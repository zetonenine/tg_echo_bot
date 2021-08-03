import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from postgresql import Database

# API_TOKEN = os.environ.get('TOKEN')
API_TOKEN = "599026278:AAGtNDoDBN_KRmK5bJ9hTfT4gD7dsazaCig"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database()


@dp.message_handler(commands=['show'])
async def count_user(message: types.Message):
    result = db.show_words()
    await message.answer(result)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    db.add_word(message.text)
    await message.answer(f"Нееее, ты {message.text}!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)