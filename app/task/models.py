from sqlalchemy import Column, Integer, String, DateTime

from app.db.base_class import Base


class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(256), nullable=True)
    due_date = Column(DateTime)
