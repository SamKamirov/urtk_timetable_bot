# import asyncio
#
# from aiogram.types import Message
# from aiogram.methods import SendMessage
# from aiogram import Router, F
#
# from Bot import bot
# router = Router()
#
# @router.message(F.text)
# async def send(message: Message):
#     await asyncio.sleep(5)
#     print(message.text)