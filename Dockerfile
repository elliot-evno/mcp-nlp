# syntax=docker/dockerfile:1
FROM ghcr.io/astral-sh/uv:python3.12-alpine AS builder

# Install the project into `/app`
WORKDIR /app

# Enable bytecode compilation and copy link mode
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Generate proper TOML lockfile first
COPY pyproject.toml README.md ./
RUN uv lock

# Then, add the rest of the project source code and install it
COPY . .
RUN uv sync --frozen --no-dev


FROM python:3.12-alpine as application

# Create a non-root user 'app'
RUN adduser -D -h /home/app -s /bin/sh app
WORKDIR /app
USER app

COPY --from=builder --chown=app:app /app/.venv /app/.venv

# Place executables in the environment at the front of the path and set PORT
ENV PATH="/app/.venv/bin:$PATH" PORT=8080

# Run the application
CMD ["sh", "-c", "mcp-nlp --transport streamable-http --host 0.0.0.0 --port ${PORT}"]
