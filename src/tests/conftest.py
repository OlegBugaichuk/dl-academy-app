from typing import Generator
import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture(scope='session')
def client() -> Generator:
    with TestClient(app) as cl:
        yield cl