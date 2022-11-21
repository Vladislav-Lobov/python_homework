import sqlite3
from logger import LOG, cancel_log


@LOG
def record_remove(id):
    """удаление записи из базы данных"""
    db = sqlite3.connect("database.db")
    db.execute("PRAGMA foreign_keys = ON;")
    cursor = db.cursor()

    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
    if not cursor.execute(sql).fetchall():
        print("\n  ошибка, создайте  файл базы данных...")
        cancel_log()
        return

    sql = f"DELETE FROM employees WHERE person_id = {id}"
    cursor.execute(sql)
    if cursor.rowcount == 0:
        print("\n Внимание! Запись для удаления не найдена... ")
        cancel_log()
    else:
        print("\n запись удалена")

    db.commit()
    db.close()
