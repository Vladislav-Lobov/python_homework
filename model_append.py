import sqlite3
from logger import LOG, cancel_log


@LOG
def record_append(new_record):
    """добавление новой записи"""
    db = sqlite3.connect("database.db")
    db.execute("PRAGMA foreign_keys = ON;")
    cursor = db.cursor()

    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
    if not cursor.execute(sql).fetchall():
        cancel_log()
        print("\n   ошибка, создайте файл базы  данных...")
        return

    sql = "INSERT INTO employees (surname, name, birthday) values(?, ?, ?)"
    data = (new_record[0], new_record[1], new_record[2])
    cursor.execute(sql, data)

    last = cursor.lastrowid
    sql = "INSERT INTO phone (phone_number, phone_person_id) values (?, ?)"
    data = (new_record[4], last)
    cursor.execute(sql, data)

    sql = "INSERT INTO positions (position, pos_person_id) values (?, ?)"
    data = (new_record[3], last)
    cursor.execute(sql, data)

    db.commit()
    db.close()

    print("\n запись добавлена ")
