import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

KEY_FILE_DIR = BASE_DIR / "auction_system" / "keys"

AUTH_OBJECT_ID = os.getenv("AUTH_OBJECT_ID")
AUCTION_OBJECT_ID = os.getenv("AUCTION_OBJECT_ID")
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
