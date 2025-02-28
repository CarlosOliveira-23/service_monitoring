from pydantic import BaseModel
from datetime import datetime


class AlertBase(BaseModel):
    service_id: int
    status: str
    message: str


class AlertCreate(AlertBase):
    pass


class AlertResponse(AlertBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
