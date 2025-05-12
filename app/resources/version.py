from fastmcp.resources import TextResource


class VersionResource(TextResource):
    """A resource that provides the version of the application."""

    def __init__(self, version: str) -> None:
        super().__init__(uri="config://version", text=version)
