# Static build of the wiki for Cabotage branch deploys (PR previews).
# Production is still GitHub Pages; see .github/workflows/docs.yml.
FROM python:3.14-slim AS build

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /src

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

COPY . .
RUN .venv/bin/sphinx-build -b html . /site -d /tmp/doctrees -j auto -q

FROM nginxinc/nginx-unprivileged:1-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /site /usr/share/nginx/html
