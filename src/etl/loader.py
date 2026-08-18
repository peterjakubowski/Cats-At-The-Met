import csv


def load_artworks_data(cursor, raw_data):

    for row in raw_data:
        artwork_id, title, artist_string, medium, date_created, tags = row
        cursor.execute('''
            INSERT INTO artworks (id, Title, Medium, "Date Created")
            VALUES (?, ?, ?, ?)
        ''', (artwork_id, title, medium, date_created))

        artist_names = [name.strip() for name in artist_string.split('|')]

        for artist_name in artist_names:
            cursor.execute('''
                INSERT OR IGNORE INTO artists (Name) VALUES (?)
            ''', (artist_name,))

            cursor.execute('''
                SELECT id FROM artists WHERE Name = ?
            ''', (artist_name,))
            artist_id = cursor.fetchone()['id']

            cursor.execute('''
                INSERT OR IGNORE INTO artwork_artists (artwork_id, artist_id)
                VALUES (?, ?)
            ''', (artwork_id, artist_id))

        tag_names = [name.strip() for name in tags.split('|')]

        for tag_name in tag_names:
            cursor.execute('''
                INSERT OR IGNORE INTO tags (Name) Values (?)
            ''', (tag_name,))

            cursor.execute('''
                SELECT id FROM tags WHERE Name = ?
            ''', (tag_name,))
            tag_id = cursor.fetchone()['id']

            cursor.execute('''
                INSERT OR IGNORE INTO artwork_tags (artwork_id, tag_id)
                VALUES (?, ?)
            ''', (artwork_id, tag_id))


def import_artworks_from_csv(cursor, file_path):

    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # next(reader)  # skip header row

        raw_data = []

        for row in reader:
            # row format: [id, title, artist_string, medium, date_created, tags]
            artwork_id = int(row['Object ID'])
            title = row['Title']
            artists = row['Artist Display Name']
            medium = row['Medium']
            date_created = row['Object Date']
            tags = row['Tags']
            raw_data.append((artwork_id, title, artists, medium, date_created, tags))

        load_artworks_data(cursor, raw_data)
