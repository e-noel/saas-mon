from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
""" from .config import settings """
import os

db_pass = os.environ.get('DATABASE_PASSWORD') or 'postgres'
#Edit this to connect to your local postgres DB

SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:{db_pass}@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
