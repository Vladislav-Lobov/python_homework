from logger import LOG, cancel_log
import sqlite3


@LOG
def export(filename):
    """экспорт базы данных в файл"""
    db = sqlite3.connect("database.db")
    db.execute("PRAGMA foreign_keys = ON;")
    cursor = db.cursor()

    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
    if not cursor.execute(sql).fetchall():
        print("\n   ошибка, создайте файл базы  данных...")
        cancel_log()
        return

    with open(filename, "w", encoding="utf-8") as data_file:
        data_base = cursor.execute("SELECT person_id, surname, name, birthday, position, phone_number "
                                    "FROM employees " 
                                    "LEFT JOIN positions ON person_id = pos_person_id "
                                    "LEFT JOIN phone ON person_id = phone_person_id ")
        for i in data_base:
            k = (str(j) for j in i)
            data_file.write(", ".join(k) + "\n")

    db.close()
    print("\n экспорт выполнен")
