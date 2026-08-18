from src.database.connection import fetch_walker_evans_cats_from_db
import pprint


def main():

    walker_evans_cats = fetch_walker_evans_cats_from_db()

    print(f"Found {len(walker_evans_cats)} results.")

    pprint.pprint(walker_evans_cats)

if __name__ == "__main__":
    main()
