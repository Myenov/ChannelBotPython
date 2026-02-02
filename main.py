import json
import asyncio
import os
from typing import Tuple

from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from dotenv import load_dotenv
from parse import parse

load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()


async def edit_post_text(mess: Message):
    parse_result = await parse(mess.text)
    await mess.edit_text(text=parse_result[0], reply_markup=parse_result[1])


async def edit_post_photo(mess: Message):
    result = None

    try:
        result = await parse(mess.caption)
    except Exception as e:
        await mess.delete()
        print(f"Error: {e}")
        return

    await mess.edit_caption(caption=result[0], reply_markup=result[1])


@dp.channel_post(F.text.startswith(".button"))
async def text_buttons_handler(mess: Message):
    asyncio.create_task(edit_post_text(mess))


@dp.channel_post(F.photo & F.caption.startswith(".button"))
async def photo_buttons_handler(mess: Message):
    asyncio.create_task(edit_post_photo(mess))


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())