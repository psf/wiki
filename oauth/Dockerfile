FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock .
RUN uv sync --no-dev --frozen

COPY app.py .

USER nobody

CMD ["/app/.venv/bin/uvicorn", "app:app", "--uds", "/var/run/cabotage/cabotage.sock"]
