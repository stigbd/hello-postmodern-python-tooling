"""Test module for root resource."""

from http import HTTPStatus

from fastapi.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_read_covered_by_test() -> None:
    """Should return 200 and message object."""
    response = client.get("/covered-by-test?covered=True")
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data["message"] == "This path is covered by a test!"
    assert data["timestamp"] is not None
    assert len(data["timestamp"]) > 0
