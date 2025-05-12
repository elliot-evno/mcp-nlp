from functools import lru_cache
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """
    Application settings.
    """

    app_name: str = "MCP-NLP Server"
    app_version: str = "0.0.1"
    instructions: str = "This server provides NLP tools."

    # See ServerSettings from fastmcp for the list of settings that can be passed
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
    )

    @property
    def fastmcp_kwargs(self) -> dict[str, Any]:
        """
        FastAPI related arguments.
        """
        return {
            "name": self.app_name,
            "instructions": self.instructions,
            "debug": self.debug,
        }


@lru_cache
def get_app_settings() -> AppSettings:
    """
    Get application settings.
    """
    return AppSettings()
