from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_grades() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.row(
        KeyboardButton(text='1 курс'),
        KeyboardButton(text='2 курс')
    )
    kb.row(
        KeyboardButton(text='3 курс'),
        KeyboardButton(text='4 курс'),
    )
    return kb.as_markup(resize_keyboard=True)
