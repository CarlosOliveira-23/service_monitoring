import pytest
from app.services.service_monitor import check_service
from app.models.service import Service


def test_check_service():
    """Test checking the status of a service."""
    service = Service(name="Google", url="https://www.google.com")
    status = check_service(service)
    assert status in ["up", "down"]
