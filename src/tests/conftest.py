import os
from typing import Iterator

import pytest
from fastapi.testclient import TestClient

from src.app.entrypoints.api import create_app
from src.app.interfaces import db


@pytest.fixture(scope="session")
def client() -> Iterator[TestClient]:
    os.environ.update(
        {"DATABASE_URL": "postgresql://postgres:mdp@adress:5432/postgres"}
    )
    app = create_app()
    client = TestClient(app)
    try:
        yield client
    finally:
        del db.DB_GATEWAY
        del db.DB
