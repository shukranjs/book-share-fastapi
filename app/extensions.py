from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sqlalchemy
from .core.settings import BaseAppSettings

settings = BaseAppSettings()

SQLALCHEMY_DATABASE_URL = settings.database_url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

metadata = sqlalchemy.MetaData()


