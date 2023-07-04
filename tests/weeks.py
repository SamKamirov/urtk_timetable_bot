import requests
from bs4 import BeautifulSoup

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
kurs_number = 1
timetables = []
timetable = ''
string = f'http://www.urtk-mephi.ru/Raspisan/'
for element in soup.find_all('li', class_=''):
    link = 'http://www.urtk-mephi.ru/' + element.find('a').get('href')
    # print(link.replace(' ', '%'))
    if string in link and 'kurs' in link:
        timetables.append(link.replace(' ', '%20', 1).removesuffix('  '))

if len(timetables) == 8:
    timetable = timetables[4:]
else:
    timetables = timetables[:4]

print(timetable)