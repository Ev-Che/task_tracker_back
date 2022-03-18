from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import get_settings

SQLALCHEMY_DATABASE_URI = (f'postgresql+psycopg2://'
                           f'{get_settings().POSTGRES_USER}:{get_settings().POSTGRES_PASSWORD}'
                           f'@localhost/postgres')

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={'check_same_thread': False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

