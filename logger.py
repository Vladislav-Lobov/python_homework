from datetime import datetime

def LOG(func):
    def wrapper(*args):
        with open('log.csv','a', encoding='utf-8') as data:
            time = datetime.now()
            data.write('функция:{0:17}  {1:55}  {2} \n'.format(func.__name__, func.__doc__, time))
        result = func(*args)
        return result
    return wrapper

def cancel_log():
    with open('log.csv','a', encoding='utf-8') as data:
            time = datetime.now()
            data.write(f'ошибка выполнения: отмена транзакции\t\t\t\t\t\t\t\t\t\t\t\t{time}\n')
