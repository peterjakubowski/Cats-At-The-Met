import sqlite3
from sqlite3 import Connection, Cursor
from src.database.schema import create_database_schema
from src.etl.loader import import_artworks_from_csv
from src.database.queries import get_walker_evans_cats
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()

PROJECT_ROOT = CURRENT_FILE.parent.parent.parent

CSV_PATH = PROJECT_ROOT / 'data' / 'MetObjects.csv'

DB_PATH = PROJECT_ROOT / 'data' / 'met_artworks.db'


def get_db_connection(db_path: Path) -> Connection:

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def is_db_initialized(cursor: Cursor) -> bool:

    cursor.execute('''
        SELECT name FROM sqlite_master
        WHERE type='table' AND name='artworks'
    ''')

    return cursor.fetchone() is not None


def fetch_walker_evans_cats_from_db() -> list[dict]:

    with get_db_connection(DB_PATH) as conn:
        cursor = conn.cursor()

        if not is_db_initialized(cursor):

            create_database_schema(cursor)

            import_artworks_from_csv(cursor, CSV_PATH)

        return get_walker_evans_cats(cursor)
