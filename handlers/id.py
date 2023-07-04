from aiogram.types import Message
from aiogram import Router

router = Router()

@router.message()
async def id(message: Message):
    print(message.from_user.id)
    print(message.chat.id)
    await message.answer(text='wweqew')