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
    timestamp: datetime = datetime.now(tz=ZoneInfo("Europe/Oslo"))


@app.get("/")
async def read_root() -> Any:
    """Get the root resource."""
    return Message(
        message="Hello world!",
    )


@app.get("/covered-by-test")
async def read_covered_by_test(covered: bool | None = None) -> Any:
    """Get the covered-by-test resource."""
    if covered:
        return Message(message="This path is covered by a test!")

    return Message(message="This path is not covered by a test!")
