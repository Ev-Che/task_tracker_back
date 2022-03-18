from functools import lru_cache

from fastapi import FastAPI

from app import config

app = FastAPI()


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
async def root():
    print(f'config: {get_settings().POSTGRES_USER}')
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
