import json
import asyncio
import os
from typing import Tuple

from aiogram import Bot, Dispatcher , F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()


async def parse(text: str) -> Tuple[str, InlineKeyboardMarkup]:
    if not text.startswith(".button:"):
        return text, None
    text_without_prefix = text[len(".button:"):]
    last_colon_index = text_without_prefix.rfind(":")

    if last_colon_index == -1:
        return text_without_prefix, None

    json_str = text_without_prefix[:last_colon_index]
    post_text = text_without_prefix[last_colon_index + 1:]

    try:
        json_data = json.loads(json_str)
        buttons_list = json_data.get("button", [])
        keyboard = []

        for row_dict in buttons_list:
            row = []
            for url, button_text in row_dict.items():
                row.append(InlineKeyboardButton(text=button_text, url=url))

            if row:
                keyboard.append(row)

        if keyboard:
            return post_text, InlineKeyboardMarkup(inline_keyboard=keyboard)
        else:
            return post_text, None

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return post_text, None
    except Exception as e:
        print(f"Error parsing buttons: {e}")
        return post_text, None


async def edit_post_text(mess: Message):
    parse_result = await parse(mess.text)
    await mess.edit_text(text=parse_result[0],reply_markup=parse_result[1])

@dp.channel_post(F.text.startswith(".button"))
async def test_handler(mess: Message):
    asyncio.create_task(edit_post_text(mess))


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())