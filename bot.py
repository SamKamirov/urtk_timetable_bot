import asyncio
import logging

from environs import Env

from aiogram import Bot, Dispatcher

from keyboardsnmenus.set_menu import set_main_menu
from handlers import grade, menu, group, id
from functions import auto_parse, ask

logging.basicConfig(level=logging.INFO)

env = Env()
env.read_env()
bot = Bot(token=env('BOT_TOKEN'))

async def main():
    dp = Dispatcher()
    # dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(grade.router, menu.router, group.router, id.router)
    # dp.include_router(auto_parse.router)

    # dp.include_routers(common.router, ordering_food.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(set_main_menu())
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())