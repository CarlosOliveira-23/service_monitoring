from fastapi import FastAPI
from app.api.endpoints import services, alerts
from app.core.database import init_db

app = FastAPI(title="Service Monitoring API")

# Include API routes
app.include_router(services.router, prefix="/services", tags=["Services"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])


@app.on_event("startup")
async def startup_event():
    """Initialize the database."""
    init_db()


@app.get("/")
async def root():
    return {"message": "Service Monitoring API is running!"}
