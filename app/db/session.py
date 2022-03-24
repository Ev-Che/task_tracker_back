from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import Settings

SQLALCHEMY_DATABASE_URI = Settings().CONNECTION_STRING
engine = create_async_engine(SQLALCHEMY_DATABASE_URI, echo=True, future=True)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    try:
        async with async_session() as session:
            yield session
    finally:
        await session.close()
