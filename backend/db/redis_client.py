import os
from pathlib import Path

from dotenv import load_dotenv
import redis

# 1. Просто загружаем .env из текущей или родительских директорий
#    python-dotenv сам его найдёт, если ты запускаешь проект из корня
load_dotenv()

# 2. Читаем настройки из окружения
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", "10778"))
REDIS_USERNAME = os.getenv("REDIS_USERNAME")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

if not REDIS_HOST:
    raise RuntimeError("REDIS_HOST is not set in .env")

# 3. Создаём синхронный клиент Redis
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    username=REDIS_USERNAME,
    password=REDIS_PASSWORD,
    decode_responses=True,  # строки вместо байтов
)
