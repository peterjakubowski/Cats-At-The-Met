from src.database.queries import get_walker_evans_cats
from .conftest import db_factory


class TestWalkerEvansCatsQueries:

    def test_get_walker_evans_cats_handles_empty_db_safely(self, db_factory):
        cursor = db_factory([])

        results = get_walker_evans_cats(cursor)

        assert results == []

    def test_get_walker_evans_cats_returns_one_result(self, db_factory):
        test_data = [
            (1, 'Cats dancing', 'Walker Evans', 'photograph', '1919-01-01', 'Cats'),
        ]

        cursor = db_factory(test_data)

        results = get_walker_evans_cats(cursor)

        assert len(results) == 1

    def test_get_walker_evans_cats_concatenates_artist_names(self, db_factory):
        test_data = [
            (1, 'Cats dancing', 'Walker Evans | Walter Nevins', 'Film Negative', '1940s', 'Cats')
        ]

        expected_results = [
            {
                'id': 1,
                'Title': 'Cats dancing',
                'Artists': 'Walker Evans, Walter Nevins',
                'Medium': 'Film Negative',
                'Date Created': '1940s',
                'Tags': 'Cats',
            }
        ]

        cursor = db_factory(test_data)

        results = get_walker_evans_cats(cursor)

        assert results == expected_results

    def test_get_walker_evans_cats_concatenates_tag_names(self, db_factory):
        test_data = [
            (1, 'Cats and birds dancing', 'Walker Evans', 'Film Negative', '1940s', 'Cats | Birds')
        ]

        expected_results = [
            {
                'id': 1,
                'Title': 'Cats and birds dancing',
                'Artists': 'Walker Evans',
                'Medium': 'Film Negative',
                'Date Created': '1940s',
                'Tags': 'Cats, Birds',
            }
        ]

        cursor = db_factory(test_data)

        results = get_walker_evans_cats(cursor)

        assert results == expected_results

    def test_get_walker_evans_cats_returns_expected_results(self, db_factory):
        test_data = [
            (1, 'Cats dancing', 'Walker Evans', 'photograph', '1919-01-01', 'Cats'),
            (2, 'Dogs dancing', 'Walker Evans', 'photograph', '1919-01-01', 'Dogs'),
            (3, 'Cats and birds dancing', 'Walker Evans', 'photograph', '1919-01-01', 'Cats|Birds'),
            (4, 'Dogs and birds dancing', 'Walker Evans', 'photograph', '1919-01-01', 'Dogs|Birds'),
            (5, 'Cats dancing', 'Walter Evans', 'photograph', '1919-01-01', 'Cats'),
            (6, 'Dogs dancing', 'Walter Evans', 'photograph', '1919-01-01', 'Dogs'),
            (7, 'Cats and birds dancing', 'Walter Evans', 'photograph', '1919-01-01', 'Cats|Birds'),
            (8, 'Dogs and birds dancing', 'Walter Evans', 'photograph', '1919-01-01', 'Dogs|Birds'),
            (9, '[2 Portraits of Jane Smith Evans Painting and 16 Portraits of a Cat, Possibly "The Boss"]',
             'Walker Evans', 'Film Negative', '1944', 'Cats'),
            (10, '', 'Walter Nevins|Walter Nevins', 'Film Negative', '', 'Birds|Birds')
        ]

        expected_results = [
            {
                'id': 1,
                'Title': 'Cats dancing',
                'Artists': 'Walker Evans',
                'Medium': 'photograph',
                'Date Created': '1919-01-01',
                'Tags': 'Cats',
            },
            {
                'id': 3,
                'Title': 'Cats and birds dancing',
                'Artists': 'Walker Evans',
                'Medium': 'photograph',
                'Date Created': '1919-01-01',
                'Tags': 'Cats, Birds',
            },
            {
                'id': 9,
                'Title': '[2 Portraits of Jane Smith Evans Painting and 16 Portraits of a Cat, '
                         'Possibly "The Boss"]',
                'Artists': 'Walker Evans',
                'Medium': 'Film Negative',
                'Date Created': 1944,
                'Tags': 'Cats',
            }
        ]

        cursor = db_factory(test_data)

        results = get_walker_evans_cats(cursor)

        assert results == expected_results
