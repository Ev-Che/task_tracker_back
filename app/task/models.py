from sqlmodel import Field

from app.task.schemas import TaskBase


class Task(TaskBase, table=True):
    id: int = Field(default=None, primary_key=True)
