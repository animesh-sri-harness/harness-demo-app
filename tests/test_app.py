import pytest
from src.app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_index_returns_ok(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"


def test_index_has_version(client):
    response = client.get("/")
    data = response.get_json()
    assert "version" in data


def test_health_returns_healthy(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert b"healthy" in response.data
