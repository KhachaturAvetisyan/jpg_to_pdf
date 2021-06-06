import glob
import logging
import os

from PIL import Image

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await msg.answer("Привет!")


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    photo = message.photo.pop()
    await photo.download()
    # raw = message.photo[-1]
    print(photo)

    # files = glob.glob('./photos/*')
    # for f in files:

        # os.remove(f)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
