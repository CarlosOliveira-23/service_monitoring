from celery import Celery
from app.services.service_monitor import update_service_status
from app.core.logging_config import logger

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def check_services():
    """Celery task to check all monitored services."""
    logger.info("Starting service monitoring task...")
    update_service_status()
    logger.info("Service monitoring task completed.")
