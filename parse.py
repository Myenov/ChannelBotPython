import json

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def parse(text: str):
    if not text.startswith(".button:"):
        return text, None
    text_without_prefix = text[len(".button:"):]
    last_colon_index = text_without_prefix.rfind(":")

    if last_colon_index == -1:
        return text_without_prefix, None

    json_str = text_without_prefix[:last_colon_index]
    post_text = text_without_prefix[last_colon_index + 1:]

    try:
        json_str_cleaned = json_str.encode('ascii', 'ignore').decode('ascii')
        json_str_cleaned = json_str_cleaned.strip()
        json_str_cleaned = json_str.replace('\xa0', ' ').replace('\u2003', ' ').replace('\u2002', ' ')

        json_data = json.loads(json_str_cleaned)
        buttons_list = json_data.get("button", [])

        keyboard = []
        for row_dict in buttons_list:
            row = []
            for url, button_text in row_dict.items():
                row.append(InlineKeyboardButton(text=button_text, url=url))

            if row:
                keyboard.append(row)

        if keyboard:
            return post_text.strip(), InlineKeyboardMarkup(inline_keyboard=keyboard)
        else:
            return post_text.strip(), None

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"JSON string (first 100 chars): {json_str[:100]}")
        print(f"JSON string (encoded): {json_str.encode('unicode_escape')}")
        return post_text.strip(), None