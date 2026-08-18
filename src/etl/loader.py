import csv
from sqlite3 import Cursor
from pathlib import Path


def load_artworks_data(cursor: Cursor, raw_data: list[dict]):

    for row in raw_data:

        artwork_id = row.get('artwork_id')
        object_number = row.get('object_number')
        title = row.get('title')
        artist_string = row.get('artists')
        medium = row.get('medium')
        date_created = row.get('date_created')
        tag_string = row.get('tags')
        department = row.get('department')
        classification_string = row.get('classification')

        cursor.execute('''
            INSERT INTO artworks (id, "Object Number", Title, Medium, "Date Created", Department)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (artwork_id, object_number, title, medium, date_created, department))

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

        tag_names = [name.strip() for name in tag_string.split('|')]

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

        classification_names = [name.strip() for name in classification_string.split('|')]

        for class_name in classification_names:
            cursor.execute('''
                INSERT OR IGNORE INTO classification (Name) Values (?)
            ''', (class_name,))

            cursor.execute('''
                SELECT id FROM classification WHERE Name = ?
            ''', (class_name,))
            class_id = cursor.fetchone()['id']

            cursor.execute('''
                INSERT OR IGNORE INTO artwork_classification (artwork_id, classification_id)
                VALUES (?, ?)
            ''', (artwork_id, class_id))


def import_artworks_from_csv(cursor: Cursor, file_path: Path):

    with open(file_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)

        raw_data = []

        for row in reader:

            artwork_object = {
                "artwork_id": int(row['Object ID']),
                "object_number": row['Object Number'],
                "title": row['Title'],
                "artists": row['Artist Display Name'],
                "medium": row['Medium'],
                "date_created": row['Object Date'],
                "tags": row['Tags'],
                "department": row['Department'],
                "classification": row['Classification']
            }

            raw_data.append(artwork_object)

        load_artworks_data(cursor, raw_data)
