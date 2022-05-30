from enum import Enum

from pydantic import BaseSettings


class Environment(Enum):
    DEV = "dev"
    PRODUCTION = "prod"


class Config(BaseSettings):
    """Read configuration from .env file
    """
    ENVIRONMENT: Environment = "DEV"
    MONGO_DB: str
    MONGO_DB_NAME: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
