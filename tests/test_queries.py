from src.database.queries import get_walker_evans_cats
from .conftest import db_factory


class TestWalkerEvansCatsQueries:

    def test_get_walker_evans_cats_handles_empty_db_safely(self, db_factory):
        cursor = db_factory([])

        results = get_walker_evans_cats(cursor)

        assert results == []

    def test_get_walker_evans_cats_returns_one_result(self, db_factory):
        test_data = [
            {
                'artwork_id': 1,
                'object_number': '10.10.10',
                'title': 'Cats dancing',
                'artists': 'Walker Evans',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats',
                'department': 'Photographs',
                'classification': 'Photographs'
            }
        ]

        cursor = db_factory(test_data)

        results = get_walker_evans_cats(cursor)

        assert len(results) == 1

    def test_get_walker_evans_cats_concatenates_artist_names(self, db_factory):
        test_data = [
            {
                'artwork_id': 1,
                'object_number': '10.10.10',
                'title': 'Cats dancing',
                'artists': 'Walker Evans | Walter Nevins',
                'medium': 'Film Negative',
                'date_created': '1940s',
                'tags': 'Cats',
                'department': 'Photographs',
                'classification': 'Photographs'
            }
        ]

        expected_results = [
            {
                'id': 1,
                'Object Number': '10.10.10',
                'Title': 'Cats dancing',
                'Artists': 'Walker Evans, Walter Nevins',
                'Medium': 'Film Negative',
                'Date Created': '1940s',
                'Tags': 'Cats',
                'Department': 'Photographs',
                'Classification': 'Photographs'
            }
        ]

        cursor = db_factory(test_data)

        results = get_walker_evans_cats(cursor)

        assert results == expected_results

    def test_get_walker_evans_cats_concatenates_tag_names(self, db_factory):
        test_data = [
            {
                'artwork_id': 1,
                'object_number': '10.10.10',
                'title': 'Cats and birds dancing',
                'artists': 'Walker Evans',
                'medium': 'Film Negative',
                'date_created': '1940s',
                'tags': 'Cats | Birds',
                'department': 'Photographs',
                'classification': 'Photographs'
            }
        ]

        expected_results = [
            {
                'id': 1,
                'Object Number': '10.10.10',
                'Title': 'Cats and birds dancing',
                'Artists': 'Walker Evans',
                'Medium': 'Film Negative',
                'Date Created': '1940s',
                'Tags': 'Cats, Birds',
                'Department': 'Photographs',
                'Classification': 'Photographs'
            }
        ]

        cursor = db_factory(test_data)

        results = get_walker_evans_cats(cursor)

        assert results == expected_results

    def test_get_walker_evans_cats_concatenates_classification_names(self, db_factory):
        test_data = [
            {
                'artwork_id': 1,
                'object_number': '10.10.10',
                'title': 'Cats dancing',
                'artists': 'Walker Evans',
                'medium': 'Film Negative',
                'date_created': '1940s',
                'tags': 'Cats',
                'department': 'Photographs',
                'classification': 'Photographs | Prints'
            }
        ]

        expected_results = [
            {
                'id': 1,
                'Object Number': '10.10.10',
                'Title': 'Cats dancing',
                'Artists': 'Walker Evans',
                'Medium': 'Film Negative',
                'Date Created': '1940s',
                'Tags': 'Cats',
                'Department': 'Photographs',
                'Classification': 'Photographs, Prints'
            }
        ]

        cursor = db_factory(test_data)

        results = get_walker_evans_cats(cursor)

        assert results == expected_results

    def test_get_walker_evans_cats_returns_expected_results(self, db_factory):

        test_data = [
            {
                "artwork_id": 1,
                "object_number": "10.10.10",
                "title": "Cats dancing",
                "artists": "Walker Evans",
                "medium": "Film Negative",
                "date_created": "1919-01-01",
                "tags": "Cats",
                "department": "Photographs",
                "classification": "Photographs"
            },

            {
                "artwork_id": 2,
                "object_number": "10.10.11",
                "title": "Dogs dancing",
                "artists": "Walker Evans",
                "medium": "photograph",
                "date_created": "1919-01-01",
                "tags": "Dogs",
                "department": "Photographs",
                "classification": "Photographs"
            },

            {
                "artwork_id": 3,
                "object_number": "10.10.12",
                "title": "Cats and birds dancing",
                "artists": "Walker Evans",
                "medium": "photograph",
                "date_created": "1919-01-01",
                "tags": "Cats|Birds",
                "department": "Photographs",
                "classification": "Photographs"
            },

            {
                "artwork_id": 4,
                "object_number": "10.10.13",
                "title": "Dogs and birds dancing",
                "artists": "Walker Evans",
                "medium": "photograph",
                "date_created": "1919-01-01",
                "tags": "Dogs|Birds",
                "department": "Photographs",
                "classification": "Photographs"
            },

            {
                "artwork_id": 5,
                "object_number": "10.10.14",
                "title": "Cats dancing",
                "artists": "Walter Evans",
                "medium": "photograph",
                "date_created": "1919-01-01",
                "tags": "Cats",
                "department": "Photographs",
                "classification": "Photographs"
            },

            {
                "artwork_id": 6,
                "object_number": "10.10.15",
                "title": "Dogs dancing",
                "artists": "Walter Evans",
                "medium": "photograph",
                "date_created": "1919-01-01",
                "tags": "Dogs",
                "department": "Photographs",
                "classification": "Photographs"
            },

            {
                "artwork_id": 7,
                "object_number": "10.10.16",
                "title": "Cats and birds dancing",
                "artists": "Walter Evans",
                "medium": "photograph",
                "date_created": "1919-01-01",
                "tags": "Cats|Birds",
                "department": "Photographs",
                "classification": "Photographs"
            },

            {
                "artwork_id": 8,
                "object_number": "10.10.17",
                "title": "Dogs and birds dancing",
                "artists": "Walter Evans",
                "medium": "photograph",
                "date_created": "1919-01-01",
                "tags": "Dogs|Birds",
                "department": "Photographs",
                "classification": "Photographs"
            },

            {
                "artwork_id": 9,
                "object_number": "10.10.18",
                "title": """[2 Portraits of Jane Smith Evans Painting and 16 Portraits of a Cat, Possibly "The Boss"]""",
                "artists": "Walker Evans",
                "medium": "Film Negative",
                "date_created": "1944-01-01",
                "tags": "Cats",
                "department": "Photographs",
                "classification": "Photographs | Paintings"
            },

            {
                "artwork_id": 10,
                "object_number": "10.10.19",
                "title": "",
                "artists": "Walter Nevins|Walter Nevins",
                "medium": "Film Negative",
                "date_created": "",
                "tags": "Birds|Birds",
                "department": "Photographs",
                "classification": "Photographs"
            }
        ]

        expected_results = [
            {
                'id': 1,
                'Object Number': '10.10.10',
                'Title': 'Cats dancing',
                'Artists': 'Walker Evans',
                'Medium': 'Film Negative',
                'Date Created': '1919-01-01',
                'Tags': 'Cats',
                'Department': 'Photographs',
                'Classification': 'Photographs'
            },
            {
                'id': 3,
                'Object Number': '10.10.12',
                'Title': 'Cats and birds dancing',
                'Artists': 'Walker Evans',
                'Medium': 'photograph',
                'Date Created': '1919-01-01',
                'Tags': 'Cats, Birds',
                'Department': 'Photographs',
                'Classification': 'Photographs'
            },
            {
                'id': 9,
                'Object Number': '10.10.18',
                'Title': '[2 Portraits of Jane Smith Evans Painting and 16 Portraits of a Cat, '
                         'Possibly "The Boss"]',
                'Artists': 'Walker Evans',
                'Medium': 'Film Negative',
                'Date Created': '1944-01-01',
                'Tags': 'Cats',
                'Department': 'Photographs',
                'Classification': 'Photographs, Paintings'
            }
        ]

        cursor = db_factory(test_data)

        results = get_walker_evans_cats(cursor)

        assert results == expected_results
