from aiogram import Router
from aiogram.types import Message
from aiogram import F


from filters.grade_filter import BackFilter
from filters.groups_filter import GroupFilter

from handlers.grade import grades

from functions.auto_parse import state


from functions.state import get_to_the_right_state

router = Router()
# sched = get_to_the_right_state()

@router.message(GroupFilter, F.text)
async def get_schedule(message: Message):
    group = state.get(message.text)
    await message.answer(text=f'Расписание группы {message.text} {group}\n\n', parse_mode='HTML')

@router.message(BackFilter, F.text)
async def back_to_courses(message: Message):
    await grades(message)