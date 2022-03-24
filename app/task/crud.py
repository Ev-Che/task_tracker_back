
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.task.models import Task


class TaskCRUD:
    @staticmethod
    async def get_all_tasks(db: AsyncSession) -> list[Task]:
        query = select(Task)
        tasks = await db.execute(query)
        return [task for task in tasks.scalars()]
