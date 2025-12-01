import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! EestiLex бот на связи 😊")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
