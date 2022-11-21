def get_menu_interface():
    print("""\n
    -----------База данных о кадрах ООО 'Светлячок'-----------
    <0> Выход из меню
    <1> Отобразить базу данных
    <2> Сгенерировать новую базу данных
    <3> Очистка/Создание новой базы данных
    <4> Добавить запись в базу
    <5> Редактировать запись базы данных
    <6> Удалить запись в базе данных
    <7> Добавить еще одну должность
    <8> Добавить еше один номер телефона
    <9> Экспорт базы данных
    <10> Импорт базы даннных
    """)


def get_menu_choice():
    return int(input("Сделайте выбор: "))


def get_new_record():
    surname = input("Введите фамилию сотрудника: ")
    name = input("Введите имя сотрудника: ")
    birthday = input("Введите день рождения сотрудника: ")
    position = input("Введите должность сотрудника: ")
    telephone = input("Введите телефон сотрудника: ")
    return (surname, name, birthday, position, telephone)


def get_id():
    return int(input("Введите id сотрудника: "))


def show_editing_id(record):
    print(f"Вы хотите изменить: {record}")


def get_position():
    return input("Введите еще одну должность: ")


def get_phone():
    return input("Введите еще один номер телефона: ")


def get_filename():
    return input("Введите имя файла: ")
