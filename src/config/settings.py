import os
from dotenv import load_dotenv

CSV_PATH = "data/pixar_films_db.csv"
TABLE_NAME = "pixar_films"


# ------------------------------
# Logging Settings
# ------------------------------

load_dotenv()

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

LOG_FILE = os.getenv("LOG_FILE", "app.log")
LOG_MAX_BYTES = int(os.getenv("LOG_MAX_BYTES", 5 * 1024 * 1024))  # 5 MB
LOG_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", 3))


OPENAI_API_KEY = f"{os.getenv('OPENAI_API_KEY')}"
OPENAI_MODEL = "gpt-3.5-turbo"
TABLE_NAME = "pixar_films"
TABLE_INFO = [
    {
        "Nome": "Title",
        "Tipo do Dado": "VARCHAR",
        "Exemplo": "Toy Story, Inside Out, Coco, Up, Finding Nemo"
    },
    {
        "Nome": "film_rating",
        "Tipo do Dado": "VARCHAR",
        "Exemplo": "G, PG, PG-13, R"
    },
    {
        "Nome": "cinema_score",
        "Tipo do Dado": "VARCHAR",
        "Exemplo": "A, A+, A-"
    },
    {
        "Nome": "Release_Date",
        "Tipo do Dado": "DATE",
        "Exemplo": "1995-11-22, 2015-06-19"
    },
    {
        "Nome": "run_time",
        "Tipo do Dado": "INT",
        "Exemplo": "81, 95, 100"
    },
    {
        "Nome": "budget",
        "Tipo do Dado": "INT",
        "Exemplo": "30000000, 20000000, 15000000"
    },
    {
        "Nome": "box_office_us_canada",
        "Tipo do Dado": "INT",
        "Exemplo": "191796233, 356461711, 200821936"
    },
    {
        "Nome": "box_office_other",
        "Tipo do Dado": "INT",
        "Exemplo": "170162503, 501100000, 301000000"
    },
    {
        "Nome": "box_office_worldwide",
        "Tipo do Dado": "INT",
        "Exemplo": "361958736, 857561711, 501821936"
    },
    {
        "Nome": "rotten_tomatoes_score",
        "Tipo do Dado": "INT",
        "Exemplo": "100, 95, 90"
    },
    {
        "Nome": "rotten_tomatoes_counts",
        "Tipo do Dado": "INT",
        "Exemplo": "100, 95, 90"
    },
    {
        "Nome": "metacritic_score",
        "Tipo do Dado": "INT",
        "Exemplo": "100, 95, 90"
    },
    {
        "Nome": "metacritic_counts",
        "Tipo do Dado": "INT",
        "Exemplo": "100, 95, 90"
    },
    {
        "Nome": "imdb_score",
        "Tipo do Dado": "FLOAT",
        "Exemplo": "8.3, 7.9, 9.0"
    },
    {
        "Nome": "imdb_counts",
        "Tipo do Dado": "INT",
        "Exemplo": "100, 95, 90"
    },
]


# ------------------------------
# Get absolute path to project root directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Define data directory and CSV path
DATA_DIR = os.path.join(ROOT_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "pixar_films_db.csv")

# Create data directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)