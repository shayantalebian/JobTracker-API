from typing import Generator
from app.core.database import SessionLocal


def get_db() -> Generator:
    """
    Creates a fresh database session for each request and closes it after the request is finished.
    """
    db = SessionLocal()
    try:
        # Hand the session over to the endpoint
        yield db
    finally:
        # Guarantee the session closes, even if the endpoint throws an error
        db.close()
