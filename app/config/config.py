import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT", "5432")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB", "postgres")
    APP_PORT: str = os.environ.get("APP_PORT", "8080")
    APP_DEBUG = os.environ.get("APP_DEBUG", False)


def get_config() -> Config:
    return Config()
