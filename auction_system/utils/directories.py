import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

OBJECT_ID = os.getenv("OBJECT_ID")
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
