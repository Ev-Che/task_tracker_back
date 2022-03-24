from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.task.crud import TaskCRUD
from app.task.schemas import TaskCreate

task_router = APIRouter(
    prefix='/tasks',
)


@task_router.get('/')
async def get_tasks(db: AsyncSession = Depends(get_session)):
    tasks = await TaskCRUD.get_all_tasks(db)
    return tasks


@task_router.post('/')
async def create_task(task: TaskCreate):
    pass
