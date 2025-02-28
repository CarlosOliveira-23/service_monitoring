import requests
from sqlalchemy.orm import Session
from app.models.service import Service
from app.services.alert_manager import create_alert
from app.core.database import SessionLocal
from app.core.logging_config import logger


def check_service(service: Service):
    """Checks the status of a given service."""
    try:
        response = requests.get(service.url, timeout=5)
        status = "up" if response.status_code == 200 else "down"
    except requests.RequestException:
        status = "down"

    return status


def update_service_status():
    """Checks all active services and updates their status."""
    db: Session = SessionLocal()
    services = db.query(Service).filter(Service.is_active == True).all()

    for service in services:
        new_status = check_service(service)

        if service.status != new_status:
            logger.info(f"Service {service.name} changed status to {new_status}")
            service.status = new_status
            db.commit()

            if new_status == "down":
                create_alert(service.id, f"🚨 {service.name} is DOWN!")

    db.close()
