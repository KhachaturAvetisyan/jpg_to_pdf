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


@dp.message_handler(commands=['convert'])
async def convert_imgs_to_pdf(message):
    # convert all images in folder ./photos to pdf
    image_list = []
    images = glob.glob('./photos/*.jpg')

    for i in images:
        image1 = Image.open(i)
        im1 = image1.convert('RGB')
        image_list.append(im1)
    image = image_list.pop(0)
    image.save('./photos/test.pdf', save_all=True, append_images=image_list)

    doc = open('./photos/test.pdf', 'rb')
    await bot.send_document(message.chat.id, doc)

    # delete all jpg file in folder ./photos
    files = glob.glob('./photos/*')
    for f in files:
        os.remove(f)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
