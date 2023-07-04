from aiogram.types import Message
from constants.values import VALUES

def GroupFilter(message: Message) -> bool:
    return message.text in VALUES