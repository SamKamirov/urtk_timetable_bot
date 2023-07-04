from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from constants.values import GROUPS


def get_groups(grade: str) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    if grade in GROUPS.keys():
        kb.row(*[KeyboardButton(text=f'{i}') for i in GROUPS[grade]])
        kb.row(KeyboardButton(text='Курсы'))
        return kb.as_markup(resize_keyboard=True)