from pydantic import BaseSettings


class Config(BaseSettings):
    """Read configuration from .env file
    """
    SQLALCHEMY_DATABASE_URL: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
