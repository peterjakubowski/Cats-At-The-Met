![Run Python Tests](https://github.com/peterjakubowski/Cats-At-The-Met/actions/workflows/ci.yaml/badge.svg)

# Cats At The Met

This project explores cats in artworks at The Met by analyzing the Metropolitan Museum of Art's [Open Access](https://github.com/metmuseum/openaccess) dataset. It consists of two main components: an Exploratory Data Analysis (EDA) of "cat" artworks in the collection, and a Test-Driven Development (TDD) framework for querying a local SQLite database of this artwork data.

## Project Overview

The repository is structured to separate the analytical exploration from the data engineering and testing framework:

1. Exploratory Data Analysis (EDA): A Jupyter Notebook (notebooks/cats_at_the_met_eda.ipynb) that dives into the dataset to discover trends of cat-related art within the Met's collection.

2. TDD Database Queries: A Python module and `pytest` suite designed to reliably load the data into an in-memory or local SQLite database and execute specific SQL queries. The primary query developed here specifically searches for cat-related artworks by the artist Walker Evans.

## Data Source: The Met Open Access CSV

The data powering this project comes directly from the Metropolitan Museum of Art's [Open Access](https://github.com/metmuseum/openaccess) initiative.The Jupyter notebook is configured to automatically download the latest `MetObjects.csv` file directly from the official Met GitHub repository upon execution. This ensures you are working with the most up-to-date publicly available collection data.

## Getting Started

### Prerequisites

Ensure you have Python 3.10+ installed. It is highly recommended to use a virtual environment.

1. Clone the repository:

```commandline
git clone https://github.com/yourusername/Cats-At-The-Met.git
cd Cats-At-The-Met
```

2. Install the required dependencies:

```commandline
pip install -r requirements.txt
```

## 1. Running the Exploratory Data Analysis (EDA)

The EDA is contained within a Jupyter Notebook.

1. Navigate to the project root and launch Jupyter Notebook:

    ```commandline
    jupyter notebook
    ```

2. Open `notebooks/cats_at_the_met_eda.ipynb` in your browser.

3. Run the cells sequentially. The initial cells will handle downloading the large `MetObjects.csv` dataset. Note: The download and initial processing may take a few minutes depending on your internet connection.

## 2. Running the TDD SQLite Framework

This section of the project uses pytest to ensure our data loading and SQL querying logic is sound before executing the main script.

### Executing the Tests

The test suite is located in the `tests/` directory and utilizes fixtures defined in `conftest.py` to create an in-memory SQLite database populated with sample data for testing purposes.

To run the test suite, execute the following command from the project root:

```commandline
pytest
```

Or, for more verbose output:

```commandline
pytest -v
```

This will run tests ensuring the schema is built correctly, data is loaded as expected, and the specific Walker Evans query returns the correct results based on the mock data.

### Running Main (The Walker Evans Query)

Once the tests pass, you can execute the main script. This script will:

1. Initialize a local SQLite database (`met_artworks.db`).
2. Load a subset of the dataset into the database.
3. Execute the target query to find artworks by Walker Evans that feature cats.

Run the main script from the project root:

```commandline
python -m src.main
```

The results of the query will be printed to the console.

### Project Structure

```
Cats-At-The-Met/
├── notebooks/
│   └── cats_at_the_met_eda.ipynb  # Jupyter notebook for EDA
├── src/
│   ├── database/                  # Database schema and queries
│   │   ├── connection.py
│   │   ├── queries.py
│   │   └── schema.py
│   ├── etl/                       # Extract, Transform, Load logic
│   │   └── loader.py
│   └── main.py                    # Entry point for the DB query execution
├── tests/                         # Pytest suite
│   ├── conftest.py                # Test fixtures (mock data, DB setup)
│   ├── test_etl.py
│   └── test_queries.py
├── requirements.txt               # Project dependencies
└── README.md                      # This file
```
