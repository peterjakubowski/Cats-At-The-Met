import sqlite3
from sqlite3 import Connection
from src.database.schema import create_database_schema
from src.etl.loader import import_artworks_from_csv
from src.database.queries import get_walker_evans_cats
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()

PROJECT_ROOT = CURRENT_FILE.parent.parent.parent

CSV_PATH = PROJECT_ROOT / 'data' / 'MetObjects.csv'


def get_db_connection() -> Connection:

    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_walker_evans_cats_from_db() -> list[dict]:

    with get_db_connection() as conn:
        cursor = conn.cursor()

        create_database_schema(cursor)

        import_artworks_from_csv(cursor, CSV_PATH)

        return get_walker_evans_cats(cursor)
