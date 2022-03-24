from functools import lru_cache

from fastapi import FastAPI, Depends

from app.config import Settings
from app.task.models import Task
from app.task.main import task_router

app = FastAPI()

app.include_router(task_router)


@lru_cache()
def get_settings():
    return Settings()


@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    print(f'config: {settings.POSTGRES_USER}')
    print(f'config: {settings.POSTGRES_PASSWORD}')
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
