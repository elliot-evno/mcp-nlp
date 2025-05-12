from fastmcp import FastMCP

from app.core.settings import get_app_settings
from app.resources.version import VersionResource
from app.tools.text_distance import textdistance_mcp


def create_application() -> FastMCP:
    """Create a FastMCP app"""
    settings = get_app_settings()

    mcp_app = FastMCP(**settings.fastmcp_kwargs)

    # Tools
    mcp_app.mount("textdistance", textdistance_mcp)
    # Resources
    mcp_app.add_resource(VersionResource(settings.app_version))

    return mcp_app


app = create_application()
# Extract the Starlette application for use with ASGI servers, like uvicorn
# ex. `uvicorn app.main:http_app --reload`
http_app = app.http_app
