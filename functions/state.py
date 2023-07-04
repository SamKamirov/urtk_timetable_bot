# from constants.values import DAYS, GROUPS
import os.path
import pandas as pd

GROUPS = {
    '1 курс': ['1АС1', '1ИС1', '1ИС2', '1ОС1', '1С1', '1Э1'],
    '2 курс': ['2АС1', '2ИС1', '2ИС2', '2ОС1', '2С1', '2Э1'],
    '3 курс': ['3ИС1', '3ОС1', '3ПИ1', '3С1'],
    '4 курс': ['4А1', '4ПИ1', '4С1']
}

DAYS = ['Понедельник\n',
        'Вторник\n',
        'Среда\n',
        'Четверг\n',
        'Пятница\n',
        'Суббота\n']

def get_to_the_right_state() -> dict:

    abs_path = os.path.dirname(__file__)

    def add_range(file_name: str, course_file):
        file_columns = list(course_file.columns)
        for i in range(len(file_columns)):
            if file_columns[i] in GROUPS[file_name]:
                for j in range(2):
                    last_elem = file_columns.pop()
                    file_columns.insert(i + 1, last_elem)
        course_file.columns = file_columns
        return file_columns


    def fill(file_name: str, columns: [], file):
        course_subj = []
        course_values = [item for item in GROUPS[file_name]]
        try:
            for column_index in range(len(columns)):
                if columns[column_index] in course_values:
                    for column_value in range(len(file[columns[column_index]])):
                        course_subj.append(
                            f'{file[columns[column_index]][column_value]}\t\t{file[columns[column_index + 1]][column_value]}'
                            f'\t\t{file[columns[column_index + 2]][column_value]}\n')
                    full_data[columns[column_index]] = course_subj
                    course_subj = []
        except IndexError:
            pass

    full_data = {}
    for file_name in GROUPS.keys():
        relative_path = f'/telegram_bot/files/{file_name}.xlsx'
        full_path = os.path.join(abs_path, relative_path)
        if os.path.isfile(full_path):
            course_file = pd.read_excel(full_path)
            file_columns = add_range(file_name, course_file)
            fill(file_name, file_columns, course_file)

    for item in full_data:
        j = 0
        course = full_data.get(item)
        day_index = 0
        while j < len(course):
            if '1' in course[j] and course[j].index('1') == 0:
                if day_index < len(DAYS):
                    course.insert(j, f'\n<strong><i>{DAYS[day_index]}</i></strong>\n')
                    day_index += 1
                j += 2
            j += 1

    for key, value in full_data.items():
        join_sus = ''.join(full_data.get(key))
        full_data[key] = join_sus

    return full_data

data = get_to_the_right_state()

# print(data)
for item in data.items():
    print(item)
