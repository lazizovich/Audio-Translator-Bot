import logging
from loader import dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

languages = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="πΊπΏ Uzbek", callback_data="uzbek_lang"),
        InlineKeyboardButton(text="π¬π§ English", callback_data="enlish_lang"),
    ]
])