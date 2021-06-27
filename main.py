import logging
import os

from aiogram import Bot, Dispatcher, executor, types
# from postgresql import BD


API_TOKEN = os.environ['TOKEN']
API_TOKEN2 = os.environ.get('TOKEN')
API_TOKEN3 = os.environ.get('TOKEN').decode('utf8')

print(API_TOKEN)
print(API_TOKEN2)
print(API_TOKEN3)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# db = BD()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        '''
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        '''

        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    # db.add_word(message.text)
    await message.answer(f"Нет, ты {message.text}!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)