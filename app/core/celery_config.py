from celery.schedules import crontab
from app.core.celery_worker import celery_app


celery_app.conf.beat_schedule = {
    "check_services_every_5_minutes": {
        "task": "app.core.celery_worker.check_services",
        "schedule": crontab(minute="*/5"),
    },
}
celery_app.conf.timezone = "UTC"
