from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import F
import asyncio
import sqlite3
import os
from dotenv import load_dotenv
from core.start.command_start import get_start
from core.gpt_answer.gpt import gpt_answer
from core.generate_mode.generate_mode import change_mode_to_text, change_mode_to_image
from data_base.create_database import create_database
load_dotenv()

TOKEN_API = os.getenv('TOKEN_API')


async def start():
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher()
    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(change_mode_to_text, F.text == '📑 Генерация текста')
    dp.message.register(change_mode_to_image, F.text == '🖼 Генерация картинок')
    dp.message.register(gpt_answer)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


async def main():
    await start()

if __name__ == '__main__':
    create_database()
    asyncio.run(main())
