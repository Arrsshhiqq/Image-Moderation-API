import pytest
from fastapi.testclient import TestClient
from Backend.main import app
from Backend.utils import get_database
from datetime import datetime
from Backend.models import Usage, Token

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    db = get_database()
    db.tokens.delete_many({})
    db.usages.delete_many({})
    db.tokens.insert_one({"token": "test-token", "is_admin": True})
    db.tokens.insert_one({"token": "user-token", "is_admin": False})

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_token():
    response = client.post(
        "/auth/tokens",
        headers={"Authorization": "Bearer test-token"},
        json={"is_admin": False}
    )
    assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
    assert "token" in response.json()

def test_moderate_image():
    with open("tests/test_image.png", "rb") as f:
        response = client.post(
            "/moderate/",
            headers={"Authorization": "Bearer user-token"},
            files={"file": ("test_image.png", f, "image/png")}
        )
    assert response.status_code == 200
    assert "moderation" in response.json()