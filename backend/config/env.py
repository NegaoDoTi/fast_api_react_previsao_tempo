from dotenv import load_dotenv
from os import getenv

load_dotenv("./backend/.env")

PORT = int(getenv("PORT"))
API_KEY_TEMPO = getenv("API_KEY_TEMPO")
DEBUG = bool(eval(getenv("DEBUG")))
DATABASE_URL = getenv("DATABASE_URL")
SECRECT_KEY = getenv("SECRECT_KEY")
ALGORITHM = getenv("ALGORITHM")