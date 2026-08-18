import sqlite3


def get_walker_evans_cats(cursor):

    query = """
        WITH filtered_artworks AS (
            SELECT 
                artworks.id,
                artworks.Title,
                artworks.Medium,
                artworks."Date Created"
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
            ) AS Tags
        FROM filtered_artworks AS fa;
    """

    cursor.execute(query)

    return [dict(row) for row in cursor.fetchall()]
