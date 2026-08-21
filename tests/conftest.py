"""Cats at The Met unit testing database

Builds an in-memory sqlite database for unit testing.

"""

__author__ = "Peter Jakubowski"

import pytest
import sqlite3
from sqlite3 import Cursor
from src.etl.loader import load_artworks_data
from src.database.schema import create_database_schema


@pytest.fixture
def db_factory():

    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    create_database_schema(cursor)

    def _populate_db(data: list[dict]) -> Cursor:
        if data:
            load_artworks_data(cursor, data)

        return cursor

    yield _populate_db

    conn.close()
