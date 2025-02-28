import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_create_alert():
    """Test creating an alert."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/alerts/", json={"service_id": 1, "status": "down", "message": "Service is down"})
    assert response.status_code == 404
