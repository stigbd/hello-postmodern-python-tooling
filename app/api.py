"""A simple server to use for testing."""

from datetime import datetime
from typing import Any
from zoneinfo import ZoneInfo

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    """The message model."""

    message: str
    timestamp: datetime


@app.get("/")
async def read_root() -> Any:
    """Get the root resource."""
    return Message(message="Hello world!", timestamp=datetime.now(tz=ZoneInfo("Europe/Oslo")))


@app.get("/covered-by-test")
async def read_covered_by_test(covered: bool | None = None) -> Any:
    """Get the covered-by-test resource."""
    timestamp = datetime.now(tz=ZoneInfo("Europe/Oslo"))

    if covered:
        return Message(message="This path is covered by a test!", timestamp=timestamp)

    return Message(message="This path is not covered by a test!", timestamp=timestamp)
