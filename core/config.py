import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "developer"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000


def get_config():
    env = os.getenv("ENV", "development")
    return env


config = get_config()