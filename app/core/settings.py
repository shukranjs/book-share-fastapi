import os
from typing import List
from dotenv import load_dotenv
import logging
from logging.config import dictConfig
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()


class BaseAppSettings(BaseSettings):
    app_name: str = "Book Share FastAPI"
    debug: bool = os.getenv("DEBUG", False)
    testing: bool = os.getenv("TESTING", False)
    database_url: str = os.getenv("DATABASE_URL")
    log_level: str = os.getenv("LOG_LEVEL", "info")
    log_format: str = "%(asctime)s - %(levelname)s - %(message)s"
    allow_origins: List[str] = ["*"]
    allow_credentials: bool = True
    allow_methods: List[str] = ["*"]
    allow_headers: List[str] = ["*"]
    database_pool_size: int = os.getenv("DATABASE_POOL_SIZE", 10)
    api_version: str = os.getenv("API_VERSION", "v1")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    use_cors_middleware: bool = os.getenv("USE_CORS_MIDDLEWARE", True)
    use_rate_limit_middleware: bool = os.getenv("USE_RATE_LIMIT_MIDDLEWARE", True)
    dependency_timeout: int = os.getenv("DEPENDENCY_TIMEOUT", 5)
    run_tests: bool = os.getenv("RUN_TESTS", False)

    def configure_logging(self):
        logging_config = {
            "version": 1,
            "formatters": {
                "default": {"format": self.log_format},
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                },
            },
            "root": {
                "level": self.log_level,
                "handlers": ["console"],
            },
        }
        dictConfig(logging_config)

    def on_startup(self):
        print("Executing startup tasks")

    def on_shutdown(self):
        print("Executing shutdown tasks")


class DevSettings(BaseAppSettings):
    debug: bool = True
    testing: bool = True
    database_url: str = os.getenv("DATABASE_URL")
    allow_origins: List[str] = ["http://localhost", "http://localhost:8000"]
    database_pool_size: int = os.getenv("DATABASE_POOL_SIZE", 5)
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "dev-secret-key")
    use_rate_limit_middleware: bool = os.getenv("USE_RATE_LIMIT_MIDDLEWARE", False)
    run_tests: bool = os.getenv("RUN_TESTS", False)

    def on_startup(self):
        super().on_startup()
        print("Additional startup tasks for development")


class ProdSettings(BaseAppSettings):
    database_url: str = os.getenv("DATABASE_URL")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY")
    run_tests: bool = os.getenv("RUN_TESTS", False)
