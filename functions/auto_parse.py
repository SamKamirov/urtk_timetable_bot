import requests
from bs4 import BeautifulSoup
import urllib.request
import tabula
import pandas as pd
import os.path
from functions.state import get_to_the_right_state
from aiogram import Router
from aiogram.types import Message
from aiogram.methods import send_message

router = Router()

def get_links() -> list:
    headers = {
        'authority': 'www.urtk-mephi.ru',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        'sec-fetch-dest': 'document',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept-language': 'en-US,en;q=0.9',
    }

    session = requests.session()

    response = session.get('http://www.urtk-mephi.ru/pages.php?id=11', headers=headers)

    if response.status_code == 200:
        print('success')
    else:
        print('error')

    soup = BeautifulSoup(response.text, 'html.parser')
    timetables = []
    timetable = ''
    string = f'http://www.urtk-mephi.ru/Raspisan/'
    for element in soup.find_all('li', class_=''):
        link = 'http://www.urtk-mephi.ru/' + element.find('a').get('href')
        if string in link and 'kurs' in link:
            timetables.append(link.replace(' ', '%20', 1).removesuffix('  '))

    if len(timetables) >= 8:
        timetable = timetables[4:]
    else:
        timetables = timetables[:4]

    return timetable


def get_files():
    # timetable = get_links()
    for i in range(1, 4, 1):
        # kurs = timetable[i]
        # print(kurs)
        # urllib.request.urlretrieve(kurs, f'/telegram_bot/files/{i+1}kurs.pdf')
        tabula.convert_into(f'/telegram_bot/files/{i+1}kurs.pdf', f'/telegram_bot/files/{i+1}kurs.csv', output_format='csv', pages='1')
        course_csv = pd.read_csv(f'/telegram_bot/files/{i+1}kurs.csv').fillna(' ')
        course_csv.to_excel(rf'/telegram_bot/files/{i+1} курс.xlsx', header=True)
    print('updated')


# get_files()
state = get_to_the_right_state()



