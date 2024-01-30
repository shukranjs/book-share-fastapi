from app.extensions import SessionLocal, metadata, engine
from sqlalchemy.orm import Session
from sqlalchemy.engine.base import Engine
from alembic.config import Config


def create_all() -> None:
    metadata.create_all(engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def close_database_connection(engine: Engine) -> None:
    engine.dispose()
