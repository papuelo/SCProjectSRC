import sqlite3

conn = sqlite3.connect('schedule.db')
cursor = conn.cursor()

while True:
    user_input = input('Ввод: ')
    if user_input == '0':
        break
    try:
        day_week, tme, type_week, subject, type_subject, teacher, group_number, room = user_input.split(', ')
        cursor.execute('''
                       INSERT INTO schedule_h(day_week, tme, type_week, subject, type_subject, teacher, group_number, room)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                       ''', (day_week, tme, type_week, subject, type_subject, teacher, group_number, room))
        conn.commit()
    except ValueError:
        print("Ошибка: введите данные в правильном формате, разделённые ', '")

cursor.execute('SELECT * FROM schedule_h')
data = cursor.fetchall()
for i in data:
    print(i)
conn.close()
