import sqlite3

conn = sqlite3.connect('../db/bot_db.db', check_same_thread=False)
cur = conn.cursor()

message = '1АС1'
data = [*cur.execute(f'Select data from timetable where group_name = "{message}"').fetchall()]
conn.close()
print(data)
