from src.database.connection import (fetch_walker_evans_cats_from_db,
                                     fetch_number_of_cat_artworks_by_artist_name_from_db,
                                     fetch_number_of_cat_artworks_by_classification_from_db)
import pprint


def main():

    walker_evans_cats = fetch_walker_evans_cats_from_db()

    print("==========================================================\n"
          f"==== Found {len(walker_evans_cats)} artworks by Walker Evans featuring cats. ====\n"
          "==========================================================\n")

    pprint.pprint(walker_evans_cats)

    number_of_cat_artworks_by_artist = fetch_number_of_cat_artworks_by_artist_name_from_db()

    print("\n\n\n"
          "==========================================\n"
          "==== Number of Cat Artworks by Artist ====\n"
          "==========================================\n")

    pprint.pprint(number_of_cat_artworks_by_artist)

    number_of_cat_artworks_by_classification = fetch_number_of_cat_artworks_by_classification_from_db()

    print("\n\n\n"
          "==================================================\n"
          "==== Number of Cat Artworks by Classification ====\n"
          "==================================================\n")

    pprint.pprint(number_of_cat_artworks_by_classification)


if __name__ == "__main__":
    main()
