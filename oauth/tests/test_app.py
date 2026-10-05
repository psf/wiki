"""Tests for the GitHub OAuth proxy."""

from __future__ import annotations

from contextlib import contextmanager
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

import pytest
from litestar.status_codes import HTTP_200_OK, HTTP_302_FOUND, HTTP_400_BAD_REQUEST
from litestar.testing import AsyncTestClient


@pytest.fixture()
def _env(monkeypatch):
    monkeypatch.setenv("GITHUB_CLIENT_ID", "test-client-id")
    monkeypatch.setenv("GITHUB_CLIENT_SECRET", "test-client-secret")


@pytest.fixture()
async def client(_env):
    # Import after env vars are set so module-level os.environ reads work
    import importlib

    import app as app_module

    importlib.reload(app_module)

    async with AsyncTestClient(app=app_module.app) as client:
        yield client


@contextmanager
def mock_github_token(token: str = "gho_test_token_123"):  # noqa: S107 - fake token for tests
    """Patch the GitHub token exchange to return *token*."""
    response = type(
        "Response",
        (),
        {
            "json": lambda self: {"access_token": token},
            "raise_for_status": lambda self: None,
        },
    )()

    async def mock_post(*args, **kwargs):
        return response

    with patch("app.httpx.AsyncClient") as mock_client_cls:
        mock_client_cls.return_value.__aenter__.return_value.post = mock_post
        yield


@contextmanager
def mock_github_error(error: str = "bad_verification_code"):
    """Patch the GitHub token exchange to return an error body (HTTP 200, no token)."""
    response = type(
        "Response",
        (),
        {
            "json": lambda self: {"error": error, "error_description": "The code is incorrect."},
            "raise_for_status": lambda self: None,
        },
    )()

    async def mock_post(*args, **kwargs):
        return response

    with patch("app.httpx.AsyncClient") as mock_client_cls:
        mock_client_cls.return_value.__aenter__.return_value.post = mock_post
        yield


def _state_from_location(location: str) -> str:
    return parse_qs(urlparse(location).query)["state"][0]


async def test_health(client):
    resp = await client.get("/_health/")
    assert resp.status_code == HTTP_200_OK
    assert resp.json() == {"status": "ok"}


async def test_auth_redirects_to_github(client):
    resp = await client.get("/auth", follow_redirects=False)
    assert resp.status_code == HTTP_302_FOUND
    location = resp.headers["location"]
    assert location.startswith("https://github.com/login/oauth/authorize")
    query = parse_qs(urlparse(location).query)
    assert query["client_id"] == ["test-client-id"]
    # Scope is fixed server-side, never the leaked Litestar ASGI ``scope`` object.
    assert query["scope"] == ["public_repo"]
    assert "ScopeState" not in location
    assert "litestar" not in location.lower()
    # CSRF: an OAuth ``state`` is always present.
    assert query["state"][0]


async def test_auth_sets_state_cookie_matching_redirect(client):
    resp = await client.get("/auth", follow_redirects=False)
    set_cookie = resp.headers["set-cookie"]
    assert "oauth_state=" in set_cookie
    assert "HttpOnly" in set_cookie
    assert "Secure" in set_cookie
    assert "SameSite=lax" in set_cookie
    assert "Path=/" in set_cookie
    # Cookie value must equal the ``state`` sent to GitHub.
    cookie_state = parse_qs(set_cookie.replace("; ", "&"))["oauth_state"][0]
    assert cookie_state == _state_from_location(resp.headers["location"])


async def test_auth_ignores_client_supplied_scope(client):
    # A caller cannot widen the requested scope (defense in depth).
    resp = await client.get("/auth?scope=repo,admin:org,delete_repo", follow_redirects=False)
    query = parse_qs(urlparse(resp.headers["location"]).query)
    assert query["scope"] == ["public_repo"]


async def test_callback_exchanges_code_for_token(client):
    auth_resp = await client.get("/auth", follow_redirects=False)
    state = _state_from_location(auth_resp.headers["location"])

    client.cookies.set("oauth_state", state, domain="testserver.local")
    with mock_github_token("gho_test_token_123"):
        resp = await client.get(f"/callback?code=test-auth-code&state={state}")

    assert resp.status_code == HTTP_200_OK
    assert "gho_test_token_123" in resp.text
    assert "authorization:github:success:" in resp.text


async def test_callback_html_is_origin_locked(client):
    state = "fixed-state-value"
    client.cookies.set("oauth_state", state, domain="testserver.local")
    with mock_github_token("gho_secret"):
        resp = await client.get(f"/callback?code=c&state={state}")
    html = resp.text
    # Token is posted only to the validated CMS origin, never to a wildcard target.
    assert '"*"' not in html
    assert "wiki.python.org" in html
    assert "isAllowed" in html


async def test_callback_success_is_not_cacheable(client):
    # The token is embedded in the response body, so it must never be cached.
    state = "cache-state"
    client.cookies.set("oauth_state", state, domain="testserver.local")
    with mock_github_token("gho_nocache"):
        resp = await client.get(f"/callback?code=c&state={state}")
    assert resp.status_code == HTTP_200_OK
    assert resp.headers["cache-control"] == "no-store"
    assert resp.headers["referrer-policy"] == "no-referrer"


async def test_callback_rejects_missing_state(client):
    with mock_github_token():
        resp = await client.get("/callback?code=test-auth-code")
    assert resp.status_code == HTTP_400_BAD_REQUEST
    assert "gho" not in resp.text


async def test_callback_rejects_mismatched_state(client):
    client.cookies.set("oauth_state", "real-value", domain="testserver.local")
    with mock_github_token():
        resp = await client.get("/callback?code=test-auth-code&state=attacker")
    assert resp.status_code == HTTP_400_BAD_REQUEST


async def test_callback_rejects_query_state_without_cookie(client):
    with mock_github_token():
        resp = await client.get("/callback?code=test-auth-code&state=lonely")
    assert resp.status_code == HTTP_400_BAD_REQUEST


async def test_callback_reports_token_exchange_failure(client):
    state = "s"
    client.cookies.set("oauth_state", state, domain="testserver.local")
    with mock_github_error("bad_verification_code"):
        resp = await client.get(f"/callback?code=bad&state={state}")
    assert resp.status_code == HTTP_400_BAD_REQUEST
    assert "OAuth token exchange failed" in resp.text
