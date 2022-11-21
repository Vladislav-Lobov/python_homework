import sqlite3
from logger import LOG, cancel_log


@LOG
def get_old_record(id):
    """поиск записи в базе данных для редактирования"""
    db = sqlite3.connect("database.db")
    cursor = db.cursor()

    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
    if not cursor.execute(sql).fetchall():
        print("\n ошибка , создайте файл базы   данных... \n")
        cancel_log()
        return -1

    sql = f"SELECT * FROM employees WHERE person_id = {id}"
    result = cursor.execute(sql).fetchall()
    if result:
        return result
    else:
        print("\n неверный id сотрудника...")
        cancel_log()
        return -1


@LOG
def record_edit(new_record, id):
    """редактирование записи базы данных"""
    db = sqlite3.connect("database.db")
    db.execute("PRAGMA foreign_keys = ON;")
    cursor = db.cursor()

    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
    if not cursor.execute(sql).fetchall():
        print("\n ошибка,  создайте файл   базы данных...")
        cancel_log()
        return

    sql = f'UPDATE employees SET surname = "{new_record[0]}" WHERE person_id = {id}'
    cursor.execute(sql)
    sql = f'UPDATE employees SET name = "{new_record[1]}" WHERE person_id = {id}'
    cursor.execute(sql)
    sql = f'UPDATE employees SET birthday = "{new_record[2]}" WHERE person_id = {id}'
    cursor.execute(sql)
    sql = f'UPDATE positions SET position = "{new_record[3]}" WHERE pos_person_id = {id}'    
    cursor.execute(sql)
    sql = f'UPDATE phone SET phone_number = "{new_record[4]}" WHERE phone_person_id = {id}'
    cursor.execute(sql)

    db.commit()
    db.close()
    print("\n редактирование записи выполнено")
