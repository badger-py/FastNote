from pydantic import BaseSettings


class Config(BaseSettings):
    """Read configuration from .env file
    """
    MONGO_DB: str
    MONGO_DB_NAME: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
