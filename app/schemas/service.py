from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime


class ServiceBase(BaseModel):
    name: str
    url: HttpUrl


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    status: Optional[str]
    is_active: Optional[bool]


class ServiceResponse(ServiceBase):
    id: int
    status: str
    is_active: bool
    created_at: datetime
    last_checked_at: Optional[datetime]

    class Config:
        from_attributes = True
