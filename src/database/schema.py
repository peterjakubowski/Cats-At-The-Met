from sqlite3 import Cursor


def create_database_schema(cursor: Cursor):

    cursor.execute('''
        CREATE TABLE artworks (
            id INTEGER PRIMARY KEY,
            "Object Number" TEXT,
            Title TEXT,
            Medium TEXT,
            "Date Created" DATE,
            Department TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE artists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE artwork_artists (
            artwork_id INTEGER,
            artist_id INTEGER,
            PRIMARY KEY (artwork_id, artist_id),
            FOREIGN KEY (artwork_id) REFERENCES artworks(id),
            FOREIGN KEY (artist_id) REFERENCES artists(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT UNIQUE
        )    
    ''')

    cursor.execute('''
        CREATE TABLE artwork_tags (
            artwork_id INTEGER,
            tag_id INTEGER,
            PRIMARY KEY (artwork_id, tag_id),
            FOREIGN KEY (artwork_id) REFERENCES artworks(id)
            FOREIGN KEY (tag_id) REFERENCES tags(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE classification (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE artwork_classification (
            artwork_id INTEGER,
            classification_id INTEGER,
            PRIMARY KEY (artwork_id, classification_id),
            FOREIGN KEY (artwork_id) REFERENCES artworks(id)
            FOREIGN KEY (classification_id) REFERENCES classification(id)
        )
    ''')
