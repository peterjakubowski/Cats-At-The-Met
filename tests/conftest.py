import pytest
import sqlite3
from src.etl.loader import load_artworks_data
from src.database.schema import create_database_schema


@pytest.fixture
def db_factory():

    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    create_database_schema(cursor)

    def _populate_db(data):
        if data:
            load_artworks_data(cursor, data)

        return cursor

    yield _populate_db

    conn.close()
