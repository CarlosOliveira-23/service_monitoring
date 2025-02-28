import pytest
from httpx import AsyncClient
from app.main import app
from app.core.database import SessionLocal, Base, engine


@pytest.fixture(scope="function", autouse=True)
def setup_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.mark.asyncio
async def test_create_service():
    """Test creating a new service."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/services/", json={"name": "Google", "url": "https://www.google.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Google"


@pytest.mark.asyncio
async def test_get_services():
    """Test retrieving services."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/services/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
