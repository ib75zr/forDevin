import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_existing_user(client):
    resp = client.get("/users/1")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"


def test_get_missing_user_returns_404(client):
    resp = client.get("/users/999")
    assert resp.status_code == 404
    data = resp.get_json()
    assert "error" in data
    assert "999" in data["error"]
