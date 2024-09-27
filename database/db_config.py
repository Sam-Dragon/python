import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///users.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_session():
    with SessionLocal() as session:
        yield session
