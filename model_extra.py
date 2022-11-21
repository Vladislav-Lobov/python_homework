import sqlite3
from logger import LOG, cancel_log


@LOG
def extra_position(position, id):
    """добавление еще одной должности сотрудника"""
    db = sqlite3.connect("database.db")
    db.execute("PRAGMA foreign_keys = ON;")
    cursor = db.cursor()

    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
    if not cursor.execute(sql).fetchall():
        print("\n ошибка, создайте файл базы данных...")
        cancel_log()
        return

    try:
        sql = f"INSERT INTO positions (position , pos_person_id) values('{position}', {id})"
        cursor.execute(sql)
        db.commit()
        print("\n запись добавлена")
    except:
        print("\n Внимание! Запись для добавления не найдена... ")
        cancel_log()
    finally:
        db.close()


@LOG
def extra_phone(phone, id):
    """добавление еще одного номера телефона сотрудника"""
    db = sqlite3.connect("database.db")
    db.execute("PRAGMA foreign_keys = ON;")
    cursor = db.cursor()

    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
    if not cursor.execute(sql).fetchall():
        print("\n ошибка  , создайте файл базы    данных...")
        cancel_log()
        return

    try:
        sql = f"INSERT INTO phone (phone_number, phone_person_id) values('{phone}', {id})"
        cursor.execute(sql)
        db.commit()
        print("\n запись добавлена")
    except:
        print("\n Внимание! Запись для добавления не найдена... ")
        cancel_log()
    finally:
        db.close()
