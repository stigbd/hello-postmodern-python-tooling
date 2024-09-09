"""Test module for the root resource."""

import time
from http import HTTPStatus
from pathlib import Path
from typing import Any

import httpx
import pytest


def is_responsive(url: str) -> bool | None:
    """Check if container is ready."""
    time.sleep(1)  # sleep a little, to let the docker container start
    try:
        response = httpx.get(url, timeout=30)
        if response.status_code == HTTPStatus.OK:
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope="session")
def http_service(docker_ip: Any, docker_services: Any) -> str:
    """Ensure that HTTP service is up and responsive."""
    # `port_for` takes a container port and returns the corresponding host port
    port = docker_services.port_for("my-api", 80)
    url = f"http://{docker_ip}:{port}"
    docker_services.wait_until_responsive(timeout=30.0, pause=0.1, check=lambda: is_responsive(url))
    return url


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig: Any) -> Any:
    """Override default location of docker-compose.yml file."""
    return Path(str(pytestconfig.rootdir), "docker-compose.yml")


def test_root(http_service: Any) -> None:
    """Should return 200 OK."""
    response = httpx.get(http_service)

    assert response.status_code == HTTPStatus.OK
    body = response.json()
    assert body["message"] == "Hello world!"
    assert body["timestamp"] is not None
