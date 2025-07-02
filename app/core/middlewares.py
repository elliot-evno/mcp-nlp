from fastmcp.server.middleware import Middleware, MiddlewareContext
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


class LoggingMiddleware(Middleware):
    """
    Middleware to log incoming requests and outgoing responses.

    This middleware logs the method, source, and message of incoming requests,
    and the result of outgoing responses. It also logs any exceptions that occur
    during the request processing.
    """

    async def on_message(self, context: MiddlewareContext, call_next):
        logger.info(
            f"Request: {context.method} | Source: {context.source} | Data: {context.message}"
        )

        try:
            result = await call_next(context)
            # Log the outgoing response
            logger.info(f"Response: {context.method} | Result: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in {context.method}: {e}", exc_info=True)
            raise
