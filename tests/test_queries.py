"""Cats at The Met SQL query unit tests

"""

__author__ = "Peter Jakubowski"

from src.database.queries import (
    count_number_of_cat_artworks_by_artist_name,
    count_number_of_cat_artworks_by_classification,
    get_walker_evans_cats,
)


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


class TestCountCatArtworksByArtists:

    def test_count_number_of_cat_artworks_by_artist_name_handles_empty_db_safely(self, db_factory):
        cursor = db_factory([])

        results = count_number_of_cat_artworks_by_artist_name(cursor)

        assert results == []

    def test_count_number_of_cat_artworks_by_artist_name_counts_one_artwork(self, db_factory):
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

        results = count_number_of_cat_artworks_by_artist_name(cursor)

        assert len(results) == 1
        assert results == [{'Artist': 'Walker Evans', 'counts': 1}]

    def test_count_number_of_cat_artworks_by_artist_name_counts_multiple_artworks_and_sorts_by_count(self, db_factory):
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
            },

            {
                'artwork_id': 2,
                'object_number': '10.10.11',
                'title': 'Cats and birds dancing',
                'artists': 'Walker Evans',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats | Birds',
                'department': 'Photographs',
                'classification': 'Photographs'
            },

            {
                'artwork_id': 3,
                'object_number': '10.10.12',
                'title': 'Cats dancing',
                'artists': 'Bob Evans',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats',
                'department': 'Photographs',
                'classification': 'Photographs'
            }
        ]

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_artist_name(cursor)

        assert results == [{'Artist': 'Walker Evans', 'counts': 2}, {'Artist': 'Bob Evans', 'counts': 1}]

    def test_count_number_of_cat_artworks_by_artist_name_returns_expected_results(self, db_factory):
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
            {'Artist': 'Walker Evans', 'counts': 3},
            {'Artist': 'Walter Evans', 'counts': 2}
        ]

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_artist_name(cursor)

        assert results == expected_results

    def test_count_number_of_cat_artworks_by_artist_name_sorts_by_artist_name_when_counts_tied(self, db_factory):
        test_data = [
            {
                'artwork_id': 1,
                'object_number': '10.10.10',
                'title': 'Cats dancing',
                'artists': 'Artist A',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats',
                'department': 'Photographs',
                'classification': 'Photographs'
            },

            {
                'artwork_id': 2,
                'object_number': '10.10.11',
                'title': 'Cats and birds dancing',
                'artists': 'Artist A',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats | Birds',
                'department': 'Photographs',
                'classification': 'Photographs'
            },

            {
                'artwork_id': 3,
                'object_number': '10.10.12',
                'title': 'Cats dancing',
                'artists': 'Artist B',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats',
                'department': 'Photographs',
                'classification': 'Photographs'
            },

            {
                'artwork_id': 4,
                'object_number': '10.10.13',
                'title': 'Cats and birds dancing',
                'artists': 'Artist B',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats | Birds',
                'department': 'Photographs',
                'classification': 'Photographs'
            }
        ]

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_artist_name(cursor)

        assert results == [{'Artist': 'Artist A', 'counts': 2}, {'Artist': 'Artist B', 'counts': 2}]

    def test_count_number_of_cat_artworks_by_artist_name_limits_10_results(self, db_factory):
        test_data = []

        for i in range(25):
            test_artwork = {
                    'artwork_id': i + 1,
                    'object_number': f'10.10.{i + 1}',
                    'title': 'Cats dancing',
                    'artists': f'Artist {chr(65 + i)}',
                    'medium': 'Film Negative',
                    'date_created': '1944-01-01',
                    'tags': 'Cats',
                    'department': 'Photographs',
                    'classification': 'Photographs'
                }
            test_data.append(test_artwork)

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_artist_name(cursor)

        assert len(results) == 10

    def test_count_number_of_cat_artworks_by_artist_name_does_not_count_artworks_with_no_artist_name(self, db_factory):
        test_data = [
            {
                'artwork_id': 1,
                'object_number': '10.10.10',
                'title': 'Cats dancing',
                'artists': '',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats',
                'department': 'Photographs',
                'classification': 'Photographs'
            }
        ]

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_artist_name(cursor)

        assert results == []


class TestCountCatArtworksByClassification:

    def test_count_number_of_cat_artworks_by_classification_handles_empty_db_safely(self, db_factory):

        cursor = db_factory([])

        results = count_number_of_cat_artworks_by_classification(cursor)

        assert results == []

    def test_count_number_of_cat_artworks_by_classification_counts_one_artwork(self, db_factory):
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

        results = count_number_of_cat_artworks_by_classification(cursor)

        assert len(results) == 1
        assert results == [{'Classification': 'Photographs', 'counts': 1}]

    def test_count_number_of_cat_artworks_by_classification_counts_for_each_class_name(self, db_factory):
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
                'classification': 'Photographs | Prints | Paintings'
            }
        ]

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_classification(cursor)

        assert len(results) == 3
        assert results == [
            {'Classification': 'Paintings', 'counts': 1},
            {'Classification': 'Photographs', 'counts': 1},
            {'Classification': 'Prints', 'counts': 1},
        ]

    def test_count_number_of_cat_artworks_by_classification_counts_multiple_artworks_and_sorts_by_count(self, db_factory):
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
            },

            {
                'artwork_id': 2,
                'object_number': '10.10.11',
                'title': 'Cats and birds dancing',
                'artists': 'Walker Evans',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats | Birds',
                'department': 'Photographs',
                'classification': 'Photographs'
            },

            {
                'artwork_id': 3,
                'object_number': '10.10.12',
                'title': 'Cats dancing',
                'artists': 'Bob Evans',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats',
                'department': 'Photographs',
                'classification': 'Paintings'
            }
        ]

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_classification(cursor)

        assert len(results) == 2
        assert results == [{'Classification': 'Photographs', 'counts': 2}, {'Classification': 'Paintings', 'counts': 1}]

    def test_count_number_of_cat_artworks_by_classification_returns_expected_results(self, db_factory):
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
                "classification": "Prints"
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
                "classification": "Prints"
            },

            {
                "artwork_id": 8,
                "object_number": "10.10.17",
                "title": "Cats, Dogs, and birds dancing",
                "artists": "Walter Evans",
                "medium": "photograph",
                "date_created": "1919-01-01",
                "tags": "Cats|Dogs|Birds",
                "department": "Photographs",
                "classification": "Prints"
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
            {'Classification': 'Photographs', 'counts': 4},
            {'Classification': 'Prints', 'counts': 2},
            {'Classification': 'Paintings', 'counts': 1},
        ]

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_classification(cursor)

        assert results == expected_results

    def test_count_number_of_cat_artworks_by_classification_sorts_by_class_when_tied(self, db_factory):
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
                'classification': 'Class A'
            },

            {
                'artwork_id': 2,
                'object_number': '10.10.11',
                'title': 'Cats and birds dancing',
                'artists': 'Walker Evans',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats | Birds',
                'department': 'Photographs',
                'classification': 'Class A'
            },

            {
                'artwork_id': 3,
                'object_number': '10.10.12',
                'title': 'Cats dancing',
                'artists': 'Walker Evans',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats',
                'department': 'Photographs',
                'classification': 'Class B'
            },

            {
                'artwork_id': 4,
                'object_number': '10.10.13',
                'title': 'Cats and birds dancing',
                'artists': 'Walker Evans',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats | Birds',
                'department': 'Photographs',
                'classification': 'Class B'
            }
        ]

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_classification(cursor)

        assert results == [{'Classification': 'Class A', 'counts': 2}, {'Classification': 'Class B', 'counts': 2}]

    def test_count_number_of_cat_artworks_by_classification_limits_10_results(self, db_factory):
        test_data = []

        for i in range(25):
            test_artwork = {
                'artwork_id': i + 1,
                'object_number': f'10.10.{i + 1}',
                'title': 'Cats dancing',
                'artists': f'Walker Evans',
                'medium': 'Film Negative',
                'date_created': '1944-01-01',
                'tags': 'Cats',
                'department': 'Photographs',
                'classification': f'Class {chr(65 + i)}'
            }
            test_data.append(test_artwork)

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_classification(cursor)

        assert len(results) == 10

    def test_count_number_of_cat_artworks_by_classification_does_not_count_artworks_with_no_class_name(self, db_factory):
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
                'classification': ''
            }
        ]

        cursor = db_factory(test_data)

        results = count_number_of_cat_artworks_by_classification(cursor)

        assert results == []
