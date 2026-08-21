"""Cats at The Met SQL queries

"""

__author__ = "Peter Jakubowski"

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


def count_number_of_cat_artworks_by_artist_name(cursor: Cursor) -> list[dict]:

    query = """
        SELECT
            artists.Name AS Artist,
            COUNT(tags.Name) AS counts
        FROM
            artworks
        RIGHT JOIN artwork_artists
            ON artworks.id = artwork_artists.artwork_id
        JOIN artists
            ON artists.id = artwork_artists.artist_id
        JOIN artwork_tags
            ON artworks.id = artwork_tags.artwork_id
        JOIN tags
            ON tags.id = artwork_tags.tag_id
        WHERE
            tags.Name = 'Cats'
        GROUP BY artists.Name
        ORDER BY counts DESC, Artist ASC
        LIMIT 10;
    """

    cursor.execute(query)

    return [dict(row) for row in cursor.fetchall()]


def count_number_of_cat_artworks_by_classification(cursor: Cursor) -> list[dict]:

    query = """
        SELECT
            classification.Name AS Classification,
            COUNT(tags.Name) AS counts
        FROM artworks
        JOIN artwork_classification
            ON artworks.id = artwork_classification.artwork_id
        JOIN classification
            ON artwork_classification.classification_id = classification.id
        JOIN artwork_tags
            ON artworks.id = artwork_tags.artwork_id
        JOIN tags
            ON artwork_tags.tag_id = tags.id
        WHERE 
            tags.Name = 'Cats'
        GROUP BY
            Classification
        ORDER BY counts DESC, Classification ASC
        LIMIT 10;
    """

    cursor.execute(query)

    return [dict(row) for row in cursor.fetchall()]
