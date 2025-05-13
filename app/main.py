from fastmcp import FastMCP
from starlette.applications import Starlette

from app.core.settings import get_app_settings
from app.resources.version import VersionResource
from app.tools.text_distance import textdistance_mcp


def create_application() -> tuple[FastMCP, Starlette]:
    """Create a FastMCP app"""
    settings = get_app_settings()

    # Configure logging
    settings.configure_logging()

    mcp_app: FastMCP = FastMCP(**settings.fastmcp_kwargs)
    # Extract the Starlette application for use with ASGI servers, like uvicorn
    starlette_app = mcp_app.http_app()

    # Tools
    mcp_app.mount("textdistance", textdistance_mcp)
    # Resources
    mcp_app.add_resource(VersionResource(settings.app_version))

    return mcp_app, starlette_app


# Create the application instance
app, http_app = create_application()
