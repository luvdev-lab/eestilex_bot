import os

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Загружаем .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/eestilex")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI is not set in .env")

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_default_database()


