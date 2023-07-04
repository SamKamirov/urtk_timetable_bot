from aiogram.types import KeyboardButton, InlineKeyboardButton, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

teachers_dict = {
    '09.02.03\nПрограммирование в компьютерных системах':'Бакирова Наталья Викторовна: Русский язык, Литература',
    '09.02.05\nПрикладная информатика (по отраслям)':'',
    '09.02.07\nИнформационные системы и программирование':'',
    '13.02.03\nЭлектрические станции, сети и системы':'',
    '14.02.01\nАтомные электрические станции и установки':'',
    '15.02.07\nАвтоматизация технологических процессов и производств (по отраслям)':'',
    '15.02.14\nОснащение средствами автоматизации технологических процессов и производств (по отраслям)':'',
    '38.02.01\nЭкономика и бухгалтерский учет (по отраслям)':''
}

def get_help():
    kb = ReplyKeyboardBuilder()
    kb.row(KeyboardButton(text='Справочная информация'))
    kb.row(KeyboardButton(text='Информация о преподавателях'))
    return kb.as_markup(resize_keyboard=True)

def get_questions():
    kb = ReplyKeyboardBuilder()
    kb.add()

def get_support():
    kb = ReplyKeyboardBuilder()
    kb.row(KeyboardButton(text='Задать вопрос разработчику'))
    kb.adjust(2, True)
    return kb.as_markup(resize_keyboard=True)

def about():
    about_text = 'Что то о проекте'

def teachers():
    kb = ReplyKeyboardBuilder()
    kb.row(KeyboardButton(text='09.02.03\nПрограммирование в компьютерных системах'))
    kb.row(KeyboardButton(text='09.02.05\nПрикладная информатика (по отраслям)'))
    kb.row(KeyboardButton(text='09.02.07\nИнформационные системы и программирование'))
    kb.row(KeyboardButton(text='13.02.03\nЭлектрические станции, сети и системы'))
    kb.row(KeyboardButton(text='14.02.01\nАтомные электрические станции и установки'))
    kb.row(KeyboardButton(text='15.02.07\nАвтоматизация технологических процессов и производств (по отраслям)'))
    kb.row(KeyboardButton(text='15.02.14\nОснащение средствами автоматизации технологических процессов и производств (по отраслям)'))
    kb.row(KeyboardButton(text='38.02.01\nЭкономика и бухгалтерский учет (по отраслям)'))
    kb.row(KeyboardButton(text='Назад'))
    return kb.as_markup(resize_keyboard=True)

def teachers_spec(message: Message):
    return teachers_dict.get(message.text)

def cancel():
    kb = ReplyKeyboardBuilder()
    kb.row(KeyboardButton(text='Отмена'))
    return kb.as_markup(resize_keyboard=True)
