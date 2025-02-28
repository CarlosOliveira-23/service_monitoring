from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import SessionLocal
from app.models.alert import Alert
from app.models.service import Service
from app.schemas.alert import AlertCreate, AlertResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AlertResponse)
def create_alert(alert: AlertCreate, db: Session = Depends(get_db)):
    """Register a new alert when a service goes down."""
    service = db.query(Service).filter(Service.id == alert.service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    new_alert = Alert(
        service_id=alert.service_id,
        status=alert.status,
        message=alert.message
    )

    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)

    return new_alert


@router.get("/", response_model=List[AlertResponse])
def list_alerts(db: Session = Depends(get_db)):
    """Retrieve all alerts."""
    return db.query(Alert).all()


@router.get("/{alert_id}", response_model=AlertResponse)
def get_alert(alert_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific alert by ID."""
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert
