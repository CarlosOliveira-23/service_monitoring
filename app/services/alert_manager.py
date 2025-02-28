from sqlalchemy.orm import Session
from app.models.alert import Alert
from app.services.telegram_bot import send_telegram_alert
from app.core.database import SessionLocal
from app.core.logging_config import logger


def create_alert(service_id: int, message: str):
    """Creates an alert and sends a notification."""
    db: Session = SessionLocal()

    alert = Alert(service_id=service_id, status="down", message=message)
    db.add(alert)
    db.commit()
    db.refresh(alert)

    send_telegram_alert(message)
    logger.warning(f"Alert created: {message}")

    db.close()
    return alert
