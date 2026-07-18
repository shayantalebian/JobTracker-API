from typing import Generator
from app.core.database import SessionLocal


def get_db() -> Generator:
    """
    Dependency that creates a new SQLAlchemy session per request
    and ensures it is closed after the request is finished.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
