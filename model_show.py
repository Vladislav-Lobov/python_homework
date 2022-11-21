import sqlite3
from logger import LOG, cancel_log


@LOG
def show_database():
    """отображение всех записей базы данных"""
    db = sqlite3.connect("database.db")

    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
    if not db.execute(sql).fetchall():
        print("\n ошибка, создайте  файл базы   данных...")
        cancel_log()
        return

    data = db.execute("SELECT person_id, surname, name, birthday, position, phone_number "
                      "FROM employees " 
                      "LEFT JOIN positions ON person_id = pos_person_id "
                      "LEFT JOIN phone ON person_id = phone_person_id ")

    data = list(data)
    data = [["id", "фамилия", "имя", "дата рождения", "должность", "номер телефона"]] + data

    print()
    for i in data:
        print("{0:<4} {1:15} {2:15} {3:15} {4:25} {5:30}".format(i[0], i[1], i[2], i[3], i[4], i[5]))

    db.close()
