import sqlite3

conn = sqlite3.connect('schedule.db')
cursor = conn.cursor()

day_week, tme, type_week, subject, type_subject, teacher, group_number, room = input('Enter:').split(', ')
cursor.execute('''
               INSERT INTO schedule_h(day_week, tme, type_week, subject, type_subject, teacher, group_number, room)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)
               ''', (day_week, tme, type_week, subject, type_subject, teacher, group_number, room)) 

conn.commit()
cursor.execute('SELECT * FROM schedule_h')
data = cursor.fetchall()
for i in data:
    print(i)
conn.close()