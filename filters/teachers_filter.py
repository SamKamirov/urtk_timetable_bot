from aiogram.types import Message
from aiogram.filters import Filter

def TeachersFilter(message: Message) -> bool:
    return message.text.lower() == 'информация о преподавателях'