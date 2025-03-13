import os

CSV_PATH = "data/pixar_films_db.csv"
TABLE_NAME = "pixar_films"


# ------------------------------
# Logging Settings
# ------------------------------

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

LOG_FILE = os.getenv("LOG_FILE", "app.log")
LOG_MAX_BYTES = int(os.getenv("LOG_MAX_BYTES", 5 * 1024 * 1024))  # 5 MB
LOG_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", 3))


OPENAI_API_KEY = ""
OPENAI_MODEL = "gpt-3.5-turbo"
TABLE_NAME = "pixar_films"
TABLE_INFO = [
    {
        "Nome": "Title",
        "Tipo do Dado": "VARCHAR",
        "Exemplo": "Toy Story, Inside Out, Coco, Up, Finding Nemo"
    },
    {
        "Nome": "Release_Year",
        "Tipo do Dado": "INT",
        "Exemplo": "1995, 2015, 2024"
    },
    {
        "Nome": "Release_Date",
        "Tipo do Dado": "DATE",
        "Exemplo": "1995-11-22, 2015-06-19"
    },
    {
        "Nome": "Director",
        "Tipo do Dado": "VARCHAR",
        "Exemplo": "John Lasseter, Pete Docter, Lee Unkrich"
    },
    {
        "Nome": "Producer",
        "Tipo do Dado": "VARCHAR",
        "Exemplo": "Bonnie Arnold, Darla K. Anderson"
    },
    {
        "Nome": "StoryWriters",
        "Tipo do Dado": "VARCHAR",
        "Exemplo": "Pete Docter, Andrew Stanton"
    },
    {
        "Nome": "Screenwriters",
        "Tipo do Dado": "VARCHAR",
        "Exemplo": "Andrew Stanton, Dan Gerson"
    },
    {
        "Nome": "Composer",
        "Tipo do Dado": "VARCHAR",
        "Exemplo": "Randy Newman, Michael Giacchino"
    },
    {
        "Nome": "Budget",
        "Tipo do Dado": "FLOAT",
        "Exemplo": "30000000, 175000000"
    },
    {
        "Nome": "BoxOffice",
        "Tipo do Dado": "FLOAT",
        "Exemplo": "373554033, 858373000, 1100000000"
    },
    {
        "Nome": "CriticRating",
        "Tipo do Dado": "FLOAT",
        "Exemplo": "8.3, 8.1, 7.5"
    },
    {
        "Nome": "OscarNominations",
        "Tipo do Dado": "INT",
        "Exemplo": "3, 2, 1"
    },
    {
        "Nome": "OscarWins",
        "Tipo do Dado": "INT",
        "Exemplo": "1, 0, 2"
    },
    {
        "Nome": "Runtime",
        "Tipo do Dado": "INT",
        "Exemplo": "81, 95, 100  # duração em minutos"
    },
    {
        "Nome": "Genre",
        "Tipo do Dado": "VARCHAR",
        "Exemplo": "Animation, Adventure, Comedy"
    }
]


# ------------------------------
# Get absolute path to project root directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Define data directory and CSV path
DATA_DIR = os.path.join(ROOT_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "pixar_films_db.csv")

# Create data directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)