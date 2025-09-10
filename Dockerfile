FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8080

WORKDIR /app
COPY . .

# install deps (supports pyproject or requirements)
RUN (pip install .) || (test -f requirements.txt && pip install -r requirements.txt) || true

# Start the server
CMD ["sh","-c","mcp-nlp --transport streamable-http --host 0.0.0.0 --port ${PORT}"]
