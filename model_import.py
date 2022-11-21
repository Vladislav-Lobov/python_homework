import sqlite3
from logger import LOG, cancel_log


@LOG
def import_from_file(filename):
    """импорт из внешнего файла"""

    db = sqlite3.connect("database.db")
    db.execute("PRAGMA foreign_keys = ON;")
    cursor = db.cursor()

    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
    if not cursor.execute(sql).fetchall():
        print("\n   ошибка, создайте файл базы  данных...")
        cancel_log()
        return

    with open(filename, "r", encoding="utf-8") as file_data:
        for i in file_data:
            new_record = i.strip().split(", ")
            sql = "INSERT INTO employees (surname, name, birthday) values(?, ?, ?)"
            data = (new_record[1], new_record[2], new_record[3])
            cursor.execute(sql, data)

            last = cursor.lastrowid
            sql = "INSERT INTO positions (position, pos_person_id) values (?, ?)"
            data = (new_record[4], last)
            cursor.execute(sql, data)

            sql = "INSERT INTO phone (phone_number, phone_person_id) values (?, ?)"
            data = (new_record[5], last)
            cursor.execute(sql, data)

            db.commit()

    db.close()
    print("\n импорт выполнен")
