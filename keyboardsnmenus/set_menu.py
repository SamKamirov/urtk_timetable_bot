from aiogram.types import BotCommand

commands = {'/start':   'Начать/Обновить',
            '/help':    'Помощь',
            '/support': 'Поддержка',
            '/about':   'О проекте'}

def set_main_menu():
    main_menu_commands = [BotCommand(command=com, description=desc) for com, desc in commands.items()]
    return main_menu_commands
