# from aiogram import Bot, Dispatcher, types
# from aiogram.filters.command import Command
# import asyncio
# import logging
# bot = Bot(token='5455946131:AAH4YSuwJqFgEF9tY_D_9pP8ZwqIzl2OTA0')
# dp = Dispatcher()
# logging.basicConfig(level=logging.INFO)
#
# import sqlite3
#
# conn = sqlite3.connect('db/bot_db.db', check_same_thread=False)
# cur = conn.cursor()
#
# data = cur.execute(f'Select group_name, data from timetable').fetchall()
# # print(data)
#
#
# def get_data(message):
#     try:
#         for i in data:
#             print(i)
#             if message in i:
#                 print(i[1])
#                 break
#     except TypeError:
#         print('error')
#
#
# get_data(input())
#
#
# def extract_data(data):
#     for i in data:
#         return i
#
#
# # print(list(map(extract_data, cur.execute('Select group_name from timetable').fetchall())))
# # print(cur.execute('Select group_name from timetable').fetchall())

