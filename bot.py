from aiogram import Bot, Dispatcher, executor, types
import pandas as pd
from API_TOKEN import API_TOKEN

GROUPS = [
    '1АС1', '1ИС1', '1ИС2', '1ОС1', '1С1', '1Э1',
    '2АС1', '2ИС1', '2ИС2', '2ОС1', '2С1', '2Э1',
    '3ИС1', '3ОС1', '3ПИ1', '3С1',
    '4А1', '4ПИ1', '4С1',
]

DAYS = ['Понедельник\n',
        'Вторник\n',
        'Среда\n',
        'Четверг\n',
        'Пятница\n',
        'Суббота\n']


a = pd.read_excel("ex.xls", sheet_name='Лист1')
a = a.to_dict('list')

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

source_row = types.ReplyKeyboardMarkup(resize_keyboard=True)
hide = types.ReplyKeyboardRemove()


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать')
    await grade(message)


async def grade(message: types.Message):
    source_row.keyboard.clear()
    source_row.row('1 курс', '2 курс')
    source_row.row('3 курс', '4 курс')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите курс',
                           reply_markup=source_row)


async def course(message: types.Message):
    source_course = message.text
    print(source_course)
    if source_course == '1 курс':
        source_row.keyboard = {}
        source_row.row('1АС1', '1ИС1', '1ИС2', '1ОС1', '1С1', '1Э1')
        source_row.row('Назад')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Выберите группу',
                               reply_markup=source_row)
    if source_course == '2 курс':
        source_row.keyboard = {}
        source_row.row('2АС1', '2ИС1', '2ИС2', '2ОС1', '2С1', '2Э1')
        source_row.add('Назад')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Выберите группу',
                               reply_markup=source_row)
    if source_course == '3 курс':
        source_row.keyboard = {}
        source_row.row('3ИС1', '3ОС1', '3ПИ1', '3С1')
        source_row.add('Назад')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Выберите группу',
                               reply_markup=source_row)
    if source_course == '4 курс':
        source_row.keyboard = {}
        source_row.row(*['4А1', '4ПИ1', '4С1'])
        source_row.add('Назад')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Выберите группу',
                               reply_markup=source_row)

    if source_course == 'Назад':
        source_row.keyboard = {}
        await grade(message)


# async def days(message: types.Message):
#     if message.text in GROUPS:
#         source_row.keyboard = {}
#         print(*DAYS[:len(DAYS)//2])
#         source_row.row(*DAYS[:len(DAYS)//2])
#         source_row.row(*DAYS[len(DAYS)//2:])
#         source_row.add('Назад')
#         await bot.send_message(chat_id=message.from_user.id,
#                                text='Выберите день',
#                                reply_markup=source_row)


async def active(message: types.Message):
    if message.text in GROUPS:
        current_course = [f'{i}\n' for i in a.get(message.text)]
        for i in range(len(current_course)):
            if current_course[i] in DAYS:
                print(current_course[i])
                current_course[i] = '*{}*'.format(current_course[i])
        print(current_course)
        # if day in current_course:
        #     for i in range(1, 6):
        #         print(current_course[current_course.index(day) + i])
        # print(current_course)
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'_Расписание группы {message.text}:_\n{"".join(i for i in current_course)}',
                               parse_mode='MarkdownV2')
    # else:
    #     await bot.send_message(chat_id=message.from_user.id,
    #                            text='Расписание отсутствует, скоро обновим.')


@dp.message_handler(content_types=['text'])
async def main(message: types.Message):
    await course(message)
    await active(message)
    # await days(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
