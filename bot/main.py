import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv
import httpx

# Загружаем .env из корня проекта
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in .env")

dp = Dispatcher()


# /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! EestiLex бот на связи 😊")


# /test_backend — проверяем связь с FastAPI
@dp.message(Command("test_backend"))
async def cmd_test_backend(message: Message):
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get("http://127.0.0.1:8000/ping")
            data = resp.json()
        await message.answer(f"Ответ от backend: {data}")
    except Exception as e:
        await message.answer(f"Не удалось подключиться к backend 😢\nОшибка: {e}")


async def main():
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
