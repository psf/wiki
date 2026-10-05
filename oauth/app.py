"""GitHub OAuth proxy for Decap CMS."""

from __future__ import annotations

import json
import os
import secrets
from pathlib import Path
from typing import Annotated
from urllib.parse import urlencode

import httpx
from litestar import Litestar, get
from litestar.datastructures import Cookie
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin
from litestar.openapi.spec import Contact, ExternalDocumentation, License, Server
from litestar.params import Parameter
from litestar.response import Redirect
from litestar.response.base import ASGIResponse

# Load .env from oauth/ or repo root if present
_env_file = Path(__file__).parent / ".env"
if not _env_file.is_file():
    _env_file = Path(__file__).parent.parent / ".env"
if _env_file.is_file():
    for line in _env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

CLIENT_ID = os.environ["GITHUB_CLIENT_ID"]
CLIENT_SECRET = os.environ["GITHUB_CLIENT_SECRET"]

AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"

# OAuth scope requested from GitHub. Hardcoded server-side so the client can never
# influence it: psf/wiki is a public repo edited via Decap/Sveltia open authoring
# (fork -> commit -> pull request), for which ``public_repo`` is the minimal scope.
OAUTH_SCOPE = "public_repo"

# Name of the short-lived cookie that ties the OAuth ``state`` across /auth -> /callback.
STATE_COOKIE = "oauth_state"

# Origins allowed to receive the access token via ``postMessage``. Defaults to the
# production CMS origin (https://wiki.python.org/edit/). Override with a
# comma-separated ``CMS_ALLOWED_ORIGINS`` env var for local development, e.g.
# ``CMS_ALLOWED_ORIGINS=http://localhost:8000``.
CMS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get("CMS_ALLOWED_ORIGINS", "https://wiki.python.org").split(",")
    if origin.strip()
]

# The callback response embeds the access token in its body, so it must never be
# cached by the browser or any intermediary, and must not leak its URL as a referrer.
NO_STORE_HEADERS = {
    "Cache-Control": "no-store",
    "Pragma": "no-cache",
    "Referrer-Policy": "no-referrer",
}

# Callback page: hands the token to the CMS window via the Decap/Sveltia postMessage
# handshake. The token is delivered ONLY to an allowlisted, origin-validated opener --
# never to an unverified origin and never with a wildcard ("*") target. Both
# placeholders are filled via ``json.dumps`` so the values are injected as safe JS
# literals (no string-escaping pitfalls, no script injection).
CALLBACK_HTML = """<!doctype html>
<html><body><script>
(function () {
  var token = __TOKEN__;
  var allowed = __ALLOWED_ORIGINS__;
  var data = JSON.stringify({ token: token, provider: "github" });
  var msg = "authorization:github:success:" + data;

  if (!window.opener) { return; }

  function isAllowed(origin) {
    return allowed.indexOf(origin) !== -1;
  }

  // Deliver the token only when our own opener, on an allowlisted origin,
  // completes the handshake -- and only back to that validated origin.
  window.addEventListener("message", function (e) {
    if (e.source !== window.opener) { return; }
    if (!isAllowed(e.origin)) { return; }
    if (e.data === "authorizing:github") {
      window.opener.postMessage(msg, e.origin);
      window.close();
    }
  }, false);

  // Announce readiness to the trusted CMS origin(s) only. This message carries no
  // token and is never broadcast with a wildcard target.
  for (var i = 0; i < allowed.length; i++) {
    window.opener.postMessage("authorizing:github", allowed[i]);
  }
})();
</script></body></html>
"""


def _render_callback(token: str) -> bytes:
    """Render the callback page, injecting the token and origin allowlist as JS literals."""
    html = CALLBACK_HTML.replace("__ALLOWED_ORIGINS__", json.dumps(CMS_ALLOWED_ORIGINS))
    html = html.replace("__TOKEN__", json.dumps(token))
    return html.encode()


def _state_cookie(value: str, max_age: int) -> Cookie:
    """Build the OAuth ``state`` cookie (set on /auth, expired on /callback)."""
    return Cookie(
        key=STATE_COOKIE,
        value=value,
        max_age=max_age,
        path="/",
        secure=True,
        httponly=True,
        samesite="lax",
    )


@get("/_health/")
async def health() -> dict[str, str]:
    """Health check endpoint for load balancers and uptime monitors.

    Returns ``{"status": "ok"}`` when the service is running.
    """
    return {"status": "ok"}


@get("/auth")
async def auth(provider: str = "github", site_id: str = "") -> Redirect:
    """Redirect the user to GitHub's OAuth authorization page.

    Decap CMS hits this endpoint to start the OAuth flow. The user gets
    sent to GitHub to approve access, then GitHub redirects back to
    :func:`callback` with an authorization code.

    A random ``state`` is generated, stored in a short-lived http-only cookie, and
    sent to GitHub; :func:`callback` verifies the echoed ``state`` against the cookie
    to defend against OAuth CSRF / code injection. The requested scope is fixed
    server-side (:data:`OAUTH_SCOPE`) and cannot be influenced by the caller.

    :param provider: OAuth provider name (passed by Decap CMS, always ``github``).
    :param site_id: Site identifier (passed by Decap CMS, unused).
    """
    state = secrets.token_urlsafe(32)
    query = urlencode({"client_id": CLIENT_ID, "scope": OAUTH_SCOPE, "state": state})
    return Redirect(f"{AUTHORIZE_URL}?{query}", cookies=[_state_cookie(state, max_age=300)])


@get("/callback", media_type="text/html")
async def callback(
    code: str,
    state_param: Annotated[str, Parameter(query="state")] = "",
    state_cookie: Annotated[str, Parameter(cookie=STATE_COOKIE)] = "",
) -> ASGIResponse:
    """Exchange a GitHub authorization code for an access token.

    GitHub redirects here after the user approves the OAuth request. The proxy
    first verifies the ``state`` echoed by GitHub against the cookie set in
    :func:`auth` (CSRF protection), then exchanges the temporary *code* for an
    access token and returns a small HTML page that ``postMessage``'s the token
    back to the CMS window -- only to an allowlisted origin.

    The parameters are deliberately *not* named ``state``/``scope``: those are
    Litestar reserved keywords and would be injected with framework objects
    instead of the request values.

    :param code: The authorization code from GitHub's OAuth redirect.
    :param state_param: The ``state`` value echoed back by GitHub (``state`` query key).
    :param state_cookie: The ``state`` value stored by :func:`auth` (cookie).
    """
    # Single-use cookie: expire it on every callback response, success or failure.
    expire = _state_cookie("", max_age=0)

    if not state_param or not state_cookie or not secrets.compare_digest(state_param, state_cookie):
        return ASGIResponse(
            body=b"OAuth state mismatch",
            media_type="text/plain",
            status_code=400,
            cookies=[expire],
            headers=NO_STORE_HEADERS,
        )

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            TOKEN_URL,
            json={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "code": code},
            headers={"Accept": "application/json"},
        )
        resp.raise_for_status()
        body = resp.json()
        token = body.get("access_token")
        if not token:
            error = body.get("error_description", body.get("error", "unknown error"))
            return ASGIResponse(
                body=f"OAuth token exchange failed: {error}".encode(),
                media_type="text/plain",
                status_code=400,
                cookies=[expire],
                headers=NO_STORE_HEADERS,
            )
    return ASGIResponse(
        body=_render_callback(token),
        media_type="text/html",
        cookies=[expire],
        headers=NO_STORE_HEADERS,
    )


app = Litestar(
    route_handlers=[health, auth, callback],
    openapi_config=OpenAPIConfig(
        title="Python Wiki API",
        version="1.0.0",
        summary="GitHub OAuth proxy powering Decap CMS for the Python Wiki.",
        description=(
            "Provides the OAuth handshake between Decap CMS (running in the browser) "
            "and GitHub, so editors can authenticate and commit changes to the wiki "
            "repository without exposing client secrets.\n\n"
            "## Endpoints\n\n"
            "| Path | Purpose |\n"
            "|---|---|\n"
            "| `GET /auth` | Redirects the user to GitHub's OAuth authorize page |\n"
            "| `GET /callback` | Exchanges the authorization code for an access token "
            "and posts it back to Decap CMS via `postMessage` |\n"
            "| `GET /_health/` | Health check for load balancers and uptime monitors |\n"
        ),
        contact=Contact(
            name="Python Software Foundation",
            url="https://www.python.org/psf/",
            email="psf@python.org",
        ),
        license=License(name="MIT", identifier="MIT"),
        external_docs=ExternalDocumentation(
            description="Python Wiki source repository",
            url="https://github.com/python/wiki",
        ),
        servers=[
            Server(url="https://api.wiki.python.org", description="Production"),
            Server(url="http://localhost:8000", description="Local development"),
        ],
        render_plugins=[ScalarRenderPlugin(path="/")],
        path="/api",
    ),
)
