from sqlite3 import Cursor


def get_walker_evans_cats(cursor: Cursor) -> list[dict]:

    query = """
        WITH filtered_artworks AS (
            SELECT 
                artworks.id,
                artworks."Object Number",
                artworks.Title,
                artworks.Medium,
                artworks."Date Created",
                artworks.Department
            FROM artworks
            JOIN artwork_artists
                ON artworks.id = artwork_artists.artwork_id
            JOIN artists
                ON artwork_artists.artist_id = artists.id
            JOIN artwork_tags
                ON artworks.id = artwork_tags.artwork_id
            JOIN tags
                ON artwork_tags.tag_id = tags.id
            WHERE artists.Name = 'Walker Evans'
                AND tags.Name = 'Cats'
        )
        SELECT
            fa.id,
            fa."Object Number",
            fa.Title,
            (
                SELECT GROUP_CONCAT(artists.Name, ', ')
                FROM artwork_artists
                JOIN artists
                    ON artwork_artists.artist_id = artists.id
                WHERE artwork_artists.artwork_id = fa.id
            ) AS Artists,
            fa.Medium,
            fa."Date Created",
            (
                SELECT GROUP_CONCAT(tags.Name, ', ')
                FROM artwork_tags
                JOIN tags
                    ON artwork_tags.tag_id = tags.id
                WHERE artwork_tags.artwork_id = fa.id
            ) AS Tags,
            fa.Department,
            (
                SELECT GROUP_CONCAT(classification.Name, ', ')
                FROM artwork_classification
                JOIN classification
                    ON artwork_classification.classification_id = classification.id
                WHERE artwork_classification.artwork_id = fa.id
            ) AS Classification
        FROM filtered_artworks AS fa;
    """

    cursor.execute(query)

    return [dict(row) for row in cursor.fetchall()]
