def create_database_schema(cursor):

    cursor.execute('''
        CREATE TABLE artworks (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Medium TEXT,
            "Date Created" DATE
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
