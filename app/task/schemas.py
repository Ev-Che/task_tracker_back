import datetime

from sqlmodel import SQLModel


class TaskBase(SQLModel):
    title: str
    description: str
    due_date: datetime.datetime


class TaskCreate(TaskBase):
    pass
