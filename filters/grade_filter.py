from aiogram.types import Message
from constants.values import GROUPS

def GradeFilter(message: Message) -> bool:
    return message.text in GROUPS.keys()

def BackFilter(message: Message) -> bool:
    return message.text.lower() == 'курсы'