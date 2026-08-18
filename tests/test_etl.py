from unittest.mock import patch, mock_open
from src.etl.loader import load_artworks_data, import_artworks_from_csv
from .conftest import db_factory


class TestLoader:

    def test_load_artworks_data_and_normalizes_artists_correctly(self, db_factory):

        cursor = db_factory([])

        raw_data = [
            (1, 'Test Art', 'Artist A | Artist B', 'oil', '2025', 'Test Tag 1')
        ]

        load_artworks_data(cursor, raw_data)

        cursor.execute('SELECT Name FROM artists')
        artists = [row['Name'] for row in cursor.fetchall()]

        assert len(artists) == 2
        assert 'Artist A' in artists
        assert 'Artist B' in artists

    def test_load_artworks_data_and_normalizes_tags_correctly(self, db_factory):
        cursor = db_factory([])

        raw_data = [
            (1, 'Test Art', 'Artist A', 'oil', '2025', 'Test Tag 1|Test Tag 2')
        ]

        load_artworks_data(cursor, raw_data)

        cursor.execute('SELECT Name FROM tags')
        tags = [row['Name'] for row in cursor.fetchall()]

        assert len(tags) == 2
        assert 'Test Tag 1' in tags
        assert 'Test Tag 2' in tags

    def test_import_artworks_from_csv_parses_and_loads(self, db_factory):

        cursor = db_factory([])

        simulated_csv_content = (
            "Object Number,Is Highlight,Is Timeline Work,Is Public Domain,Object ID,Gallery Number,Department,AccessionYear,Object Name,Title,Culture,Period,Dynasty,Reign,Portfolio,Constituent ID,Artist Role,Artist Prefix,Artist Display Name,Artist Display Bio,Artist Suffix,Artist Alpha Sort,Artist Nationality,Artist Begin Date,Artist End Date,Artist Gender,Artist ULAN URL,Artist Wikidata URL,Object Date,Object Begin Date,Object End Date,Medium,Dimensions,Credit Line,Geography Type,City,State,County,Country,Region,Subregion,Locale,Locus,Excavation,River,Classification,Rights and Reproduction,Link Resource,Object Wikidata URL,Metadata Date,Repository,Tags,Tags AAT URL,Tags Wikidata URL\n"
            "1920.1.1,False,False,True,101,,Paintings,1920,Painting,Water Lilies and Whiskers,,,,,,111,Artist,,Clawdia Monet,French 1840-1926,,Monet Clawdia,French,1840,1926,,,,1919,1919,1919,Oil on canvas,100 x 200 cm,Gift of Feline Friends,,,,,,,,,,,Paintings,,,2026-08-17,Metropolitan Museum of Art,Cats|Flowers,,\n"
            "1938.2.2,False,False,False,102,,Paintings,1938,Painting,Guernicat,,,,,,222,Artist,,Pablo Picatso,Spanish 1881-1973,,Picatso Pablo,Spanish,1881,1973,,,,1937,1937,1937,Oil on canvas,349 x 776 cm,Gift of the Artist,,,,,,,,,,,Paintings,,,2026-08-17,Metropolitan Museum of Art,Cats|Abstract,,\n"
            "1950.3.3,False,False,True,103,,Paintings,1950,Painting,Dogs Playing Poker,,,,,,333,Artist,,C.M. Coolidge,American 1844-1913,,Coolidge C.M.,American,1844,1913,,,,1903,1903,1903,Oil on canvas,100 x 120 cm,Gift of Canines,,,,,,,,,,,Paintings,,,2026-08-17,Metropolitan Museum of Art,Dogs|Games,,\n"
        )

        m_open = mock_open(read_data=simulated_csv_content)

        with patch('builtins.open', m_open):

            import_artworks_from_csv(cursor, "fake_path/artworks.csv")

        cursor.execute('SELECT COUNT(*) as count FROM artworks')

        assert cursor.fetchone()['count'] == 3

        cursor.execute('SELECT Name FROM artists')
        artists = [row['Name'] for row in cursor.fetchall()]
        assert 'Clawdia Monet' in artists
        assert 'Pablo Picatso' in artists
        assert 'C.M. Coolidge' in artists
