import os
from dotenv import load_dotenv
import pandas as pd

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
        "Nome": "film",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Nome do filme",
        "Exemplo": "Toy Story, Inside Out, Up"
    },
    {
        "Nome": "number",
        "Tipo do Dado": "INT",
        "Descricao": "Identificador numérico do filme",
        "Exemplo": "1, 2, 3"
    },
    {
        "Nome": "release_date",
        "Tipo do Dado": "DATE",
        "Descricao": "Data de lançamento do filme",
        "Exemplo": "1995-11-22, 2015-06-19, 2009-05-29"
    },
    {
        "Nome": "run_time",
        "Tipo do Dado": "INT",
        "Descricao": "Duração do filme em minutos",
        "Exemplo": "81, 94, 96"
    },
    {
        "Nome": "film_rating",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Classificação do filme",
        "Exemplo": "G, PG, PG-13"
    },
    {
        "Nome": "plot",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Sinopse do filme",
        "Exemplo": "A cowboy doll is profoundly threatened and jealous when a new spaceman figure sup"
    },
    {
        "Nome": "category",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Se é genero ou subgenero do filme",
        "Exemplo": "Genre, Subgenre"
    },
    {
        "Nome": "value",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Genero ou subgenero do filme",
        "Exemplo": "Animation, Adventure, Comedy"
    },
    {
        "Nome": "budget",
        "Tipo do Dado": "INT",
        "Descricao": "Orçamento do filme em milhões de dólares",
        "Exemplo": "30000000, 20000000, 175000000"
    },
    {
        "Nome": "box_office_us_canada",
        "Tipo do Dado": "INT",
        "Descricao": "Bilheteria do filme nos EUA e Canadá em milhões de dólares",
        "Exemplo": "191796233, 356461711, 293004164"
    },
    {
        "Nome": "box_office_other",
        "Tipo do Dado": "INT",
        "Descricao": "Bilheteria do filme em outros países em milhões de dólares",
        "Exemplo": "181757800, 541000000, 438338580"
    },
    {
        "Nome": "box_office_worldwide",
        "Tipo do Dado": "INT",
        "Descricao": "Bilheteria do filme no mundo todo em milhões de dólares",
        "Exemplo": "373554033, 897461711, 731342744"
    },
    {
        "Nome": "rotten_tomatoes_score",
        "Tipo do Dado": "INT",
        "Descricao": "Nota do filme no Rotten Tomatoes",
        "Exemplo": "100, 98, 96"
    },
    {
        "Nome": "rotten_tomatoes_counts",
        "Tipo do Dado": "INT",
        "Descricao": "Quantidade de avaliações no Rotten Tomatoes",
        "Exemplo": "78, 306, 287"
    },
    {
        "Nome": "metacritic_score",
        "Tipo do Dado": "INT",
        "Descricao": "Nota do filme no Metacritic",
        "Exemplo": "95, 94, 96"
    },
    {
        "Nome": "metacritic_counts",
        "Tipo do Dado": "INT",
        "Descricao": "Quantidade de avaliações no Metacritic",
        "Exemplo": "26, 41, 39"
    },
    {
        "Nome": "cinema_score",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Classificação do CinemaScore",
        "Exemplo": "A+, A, A-"
    },
    {
        "Nome": "imdb_score",
        "Tipo do Dado": "FLOAT",
        "Descricao": "Nota do filme no IMDb",
        "Exemplo": "8.3, 8.0, 7.9"
    },
    {
        "Nome": "imdb_counts",
        "Tipo do Dado": "INT",
        "Descricao": "Quantidade de avaliações no IMDb",
        "Exemplo": "1, 2, 3"
    },
    {
        "Nome": "Director",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Diretor do filme",
        "Exemplo": "John Lasseter, Pete Docter, Andrew Stanton"
    },
    {
        "Nome": "Musician",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Músico responsável pela trilha sonora do filme",
        "Exemplo": "Randy Newman, Michael Giacchino, Thomas Newman"
    },
    {
        "Nome": "Producer",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Produtor do filme",
        "Exemplo": "Darla K. Anderson, Jonas Rivera, Mark Nielsen"
    },
    {
        "Nome": "Screenwriter",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Roteirista do filme",
        "Exemplo": "Andrew Stanton, Pete Docter, Lee Unkrich"
    },
    {
        "Nome": "Storywriter",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Escritor da história do filme",
        "Exemplo": "John Lasseter, Pete Docter, Andrew Stanton"
    },
    {
        "Nome": "Co-director",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Co-diretor do filme",
        "Exemplo": "Andrew Stanton, Lee Unkrich, Ash Brannon"
    },
    {
        "Nome": "Animated_Feature",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Se ganhou ou foi indicado ao oscar de Melhor Animação",
        "Exemplo": "Won, Nominated, Ineligible, Award not yet introduced"
    },
    {
        "Nome": "Original_Screenplay",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Se ganhou ou foi indicado ao oscar de Melhor Roteiro Original",
        "Exemplo": "Won, Nominated, Ineligible, Award not yet introduced"
    },
    {
        "Nome": "Adapter_Screenplay",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Se ganhou ou foi indicado ao oscar de Melhor Roteiro Adaptado",
        "Exemplo": "Won, Nominated, Ineligible, Award not yet introduced"
    },
    {
        "Nome": "Original_Score",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Se ganhou ou foi indicado ao oscar de Melhor Trilha Sonora Original",
        "Exemplo": "Won, Nominated, Ineligible, Award not yet introduced"
    },
    {
        "Nome": "Original_Song",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Se ganhou ou foi indicado ao oscar de Melhor Canção Original",
        "Exemplo": "Won, Nominated, Ineligible, Award not yet introduced"
    },
    {
        "Nome": "Other",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Outros prêmios ganhos ou indicados",
        "Exemplo": "Won, Nominated, Ineligible, Award not yet introduced"
    },
    {
        "Nome": "Sound_Editing",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Se ganhou ou foi indicado ao oscar de Melhor Edição de Som",
        "Exemplo": "Won, Nominated, Ineligible, Award not yet introduced"
    },
    {
        "Nome": "Sound_Mixing",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Se ganhou ou foi indicado ao oscar de Melhor Mixagem de Som",
        "Exemplo": "Won, Nominated, Ineligible, Award not yet introduced"
    },
    {
        "Nome": "Best_Picture",
        "Tipo do Dado": "VARCHAR",
        "Descricao": "Se ganhou ou foi indicado ao oscar de Melhor Filme",
        "Exemplo": "Won, Nominated, Ineligible, Award not yet introduced"
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