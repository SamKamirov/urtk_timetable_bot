from aiogram import Router
from aiogram import F
from aiogram.types import Message

from keyboardsnmenus.for_grades import get_grades
from keyboardsnmenus.for_groups import get_groups

from filters.grade_filter import GradeFilter

router = Router()

@router.message(GradeFilter, F.text)
async def groups(message: Message):
    await message.answer(
        text=f'Выберите группу',
        reply_markup=get_groups(message.text)
    )

async def grades(message: Message):
    await message.answer(
        text=f'Выберите курс',
        reply_markup=get_grades()
    )