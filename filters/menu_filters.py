from aiogram.types import Message
from aiogram.filters import Filter


def HelpFilter(message: Message) -> bool:
    return message.text == 'Раздел "Помощь"'

def FAQ(message: Message) -> bool:
    return message.text == 'Справочная информация'