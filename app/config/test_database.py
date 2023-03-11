from unittest import mock

import pytest
import os
from .database import PSQLConfig


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    with mock.patch.dict(
        os.environ,
        {
            "POSTGRES_USER": "postgres",
            "POSTGRES_PASSWORD": "postgres",
            "POSTGRES_SERVER": "db",
            "POSTGRES_PORT": "5432",
            "POSTGRES_DB": "postgres",
        },
    ):
        yield


def test_psql_config():
    config = PSQLConfig()
    assert config.dsn == "postgresql://postgres:postgres@db:5432/postgres"
