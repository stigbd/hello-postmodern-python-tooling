"""Test module for the root resource."""

from http import HTTPStatus

from fastapi.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_read_root() -> None:
    """Should return OK and a message object."""
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data["message"] == "Hello world!"
    assert data["timestamp"] is not None
    assert len(data["timestamp"]) > 0
