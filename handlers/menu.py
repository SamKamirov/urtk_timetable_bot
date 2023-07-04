import logging

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, Text

from keyboardsnmenus.for_grades import get_grades
from keyboardsnmenus.for_menu import get_help, get_support, teachers, cancel

from filters.teachers_filter import TeachersFilter
from filters.menu_filters import HelpFilter, FAQ

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboardsnmenus.for_menu import teachers_spec
from constants.values import VALUES

from Bot import bot

router = Router()

class Form(StatesGroup):
    support = State()
    get_message = State()
    program = State()


@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        'Добро пожаловать\nВыберите курс',
        reply_markup=get_grades()
    )


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        'Раздел "Помощь"\n\nВ данном разделе вы сможете найти всю интересующую вас информацию',
        reply_markup=get_help()
    )


@router.message(Command('support'))
async def cmd_support(message: Message, state: FSMContext):
    await state.set_state(Form.support)
    await message.answer(
        'Раздел "Поддержка"\n\nВ данном разделе вы сможете обратиться к разработчику, если у вас возникнут проблемы',
        reply_markup=get_support()
    )


@router.message(Form.support, Text(text='Задать вопрос разработчику'))
async def ask_dev(message: Message, state: FSMContext):
    await state.set_state(Form.get_message)
    print(message.chat.id)
    await message.answer('Режим "Вопрос"\n\nВведите своё имя, фамилию, группу и само сообщение.\n\nВведите сообщение для отправки:',
                         reply_markup=cancel())


@router.message(Form.get_message, Text(text='Отмена'))
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Отменяем состояние %r', current_state)
    await state.clear()
    await message.answer('Отменено', reply_markup=ReplyKeyboardRemove())


@router.message(Form.get_message)
async def proccess_message(message: Message, state: FSMContext):
    for i in VALUES:
        if i in message.text:
            await bot.send_message(text=f'Вопрос от пользователя '
                                f'{message.from_user.first_name} {message.from_user.last_name}\n\n'
                                f'{message.text}?', chat_id=-1001920566357)
            await message.answer('Спасибо за вопрос. Ответ будет отправлен в ближайшее время.', reply_markup=ReplyKeyboardRemove())
            await state.clear()


@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer(
        'Раздел "О проекте"\n\n'
        'Написано на Python 3.9 и Aiogram v3.0 beta 7\n'
        'Разработал студент группы 3ИС1 Камиров Семён.'
    )

@router.message(TeachersFilter)
async def teachers_info(message: Message, state: FSMContext):
    await state.set_state(Form.program)
    current_state = await state.get_state()
    print('State %r', current_state)

    if current_state is None:
        return

    await message.answer(
        'Выберите специальность',
        reply_markup=teachers()
    )



@router.message(FAQ)
async def guide(message: Message):
    await message.answer('Справочная информация\n\n'
                         'Для получения доступа к командам нажмите на меню слева или введите символ "/" в строке набора сообщений.\n\n'
                         '<b>/help</b>\n\n'
                         'Выводит справочную информацию и предоставляет доступ к информации о преподавателях\n\n'
                         '<b>/support</b>\n\n'
                         'Позволяет оставить вопрос разработчику в случае возникновения проблемы в работе бота. Также вы можете оставить пожелание для улучшения бота (добавление функций, и т.д.)\n\n'
                         '<b>/about</b>\n\n'
                         'Выводит общую информацию о проекте',
                         parse_mode='HTML')


@router.message(Form.program, Text('Назад'))
async def back_to_help(message: Message, state: FSMContext):
    # current_state = await state.get_state()
    #
    # if current_state is None:
    #     return
    #
    # logging.info('Возвращаюсь назад', current_state)
    await state.clear()
    await cmd_help(message)


@router.message(Form.program)
async def get_teachers(message: Message):
    if message.text != 'Назад':
        current_teachers = teachers_spec(message)
        print(current_teachers)
        if current_teachers == '':
            return
        await message.answer(text=f'{current_teachers}')

@router.message(HelpFilter, F.text)
async def back(message: Message):
    await cmd_help(message)