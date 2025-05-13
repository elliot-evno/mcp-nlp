from loguru import logger
from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse


class ApiKeyAuthMiddleware(BaseHTTPMiddleware):
    """
    Middleware to check for API key in the request headers.

    If the API key is missing or invalid, a 401 Unauthorized response is returned.
    """

    def __init__(self, app, api_key: str, api_key_name: str = "X-API-Key"):
        super().__init__(app)
        self.api_key = api_key
        self.api_key_name = api_key_name

    async def dispatch(self, request: Request, call_next):
        # Check for API key in header
        api_key = request.headers.get(self.api_key_name)
        if api_key != self.api_key:
            logger.error(f"Invalid API key provided: {api_key}")
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Invalid or missing API key"},
            )

        return await call_next(request)
