import logging
import sys
from functools import lru_cache
from typing import Any, Literal

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.logging import InterceptHandler


class AppSettings(BaseSettings):
    """
    Application settings.
    """

    app_name: str = "MCP-NLP Server"
    app_version: str = "0.0.1"
    instructions: str = "This server provides NLP tools."

    transport: Literal["streamable-http", "sse"] = "streamable-http"

    allowed_hosts: list[str] = ["*"]

    # See ServerSettings from fastmcp for the list of settings that can be passed
    debug: bool = False

    # API key authentication
    api_key_enabled: bool = False
    api_key: str | None = None
    api_key_name: str = "X-API-Key"  # Header name

    logging_level: int = logging.INFO
    loggers: tuple[str, ...] = ("uvicorn.asgi", "uvicorn.access")

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

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]

        # Disable all other handlers
        logger.remove()
        # Add Loguru handler
        logger.add(sys.stderr, level=self.logging_level)


@lru_cache
def get_app_settings() -> AppSettings:
    """
    Get application settings.
    """
    return AppSettings()
