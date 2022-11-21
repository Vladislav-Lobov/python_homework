import sqlite3
from logger import LOG

@LOG
def create_database():
    '''создание таблиц баз данных'''
    db = sqlite3.connect('database.db')
    
    db.execute('CREATE TABLE IF NOT EXISTS employees ('
               'person_id INTEGER PRIMARY KEY AUTOINCREMENT, '
               'surname TEXT NOT NULL, '
               'name TEXT NOT NULL, '
               'birthday TEXT NOT NULL) ')

    db.execute('CREATE TABLE IF NOT EXISTS positions ('
               'position TEXT NOT NULL,'
               'pos_person_id INTEGER NOT NULL,'
               'FOREIGN KEY (pos_person_id) REFERENCES employees (person_id) ON DELETE CASCADE ON UPDATE CASCADE)')

    db.execute('CREATE TABLE IF NOT EXISTS phone ('
               'phone_number TEXT NOT NULL,'
               'phone_person_id INTEGER NOT NULL, '
               'FOREIGN KEY (phone_person_id) REFERENCES employees (person_id) ON DELETE CASCADE ON UPDATE CASCADE)')
     

    db.commit()
    db.close()
    print('\n база создана')

@LOG
def clear_database():
    '''удаление таблиц базы данных'''
    db = sqlite3.connect('database.db')
    db.execute("DROP table IF EXISTS employees")
    db.execute("DROP table IF EXISTS positions")
    db.execute("DROP table IF EXISTS phone")

    db.commit()
    db.close()
    print('\n база удалена')


