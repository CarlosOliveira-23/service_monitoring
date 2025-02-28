from sqlalchemy.orm import Session
from fastapi import Depends
from app.core.database import SessionLocal


def get_db():
    """Dependency to provide a database session in API endpoints."""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
