# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"  # Load environment variables from .env file

# Create an instance of Settings to be used throughout the application
settings = Settings()
