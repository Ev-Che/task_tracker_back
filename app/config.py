import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    load_dotenv(dotenv_path=".env")

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')

    CONNECTION_STRING: str = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db/postgres'
