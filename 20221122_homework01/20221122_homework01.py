# Домашняя работа от 22 ноября 2022 года. (семинар №9)
# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

from tkinter import Button, Tk, Label

winner_x = 0
winner_o = 0
counter = 0
field = []

form = Tk()
form.title('Крестики и нолики')

# основная надпись:
alert_label = Label(form, text='Игра началась', justify='left', borderwidth=9)
alert_label.grid(row=0, column=1, columnspan=2)

# счет
label_x = Label(form, text='X:0', justify='left', borderwidth=9)
label_x.grid(row=0, column=0)
label_o = Label(form, text='O:0', justify='right', borderwidth=9)
label_o.grid(row=0, column=3)


def make_buttons():
    index = 0
    for row in range(1, 4):
        for col in range(0, 3):
            button = Button(form,
                            text=' ',
                            width=4,
                            height=2,
                            font=('Verdana', 20, 'bold'),
                            background='lavender',
                            command=lambda x=index: proccess(x))
            button.grid(row=row, column=col, sticky='nsew')
            field.append(button)
            index += 1

    new_button = Button(form, text='Новая \nигра', width=6, command=new_game)
    new_button.grid(row=1, column=3, rowspan=3, sticky='nsew')


def take_input(XO, position):
    global counter
    if (field[position]['text'] not in "XO"):
        field[position]['text'] = XO
    else:
        alert_label['text'] = "Клеточка уже занята..."
        counter -= 1


def check_win(field):
    win_coord = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                 [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for each in win_coord:
        if field[each[0]]['text'] == field[each[1]]['text'] == field[each[2]]['text'] != ' ':
            return field[each[0]]['text']
    return False


def proccess(position):
    global counter, winner_x, winner_o
    if counter % 2 == 0:
        alert_label['text'] = 'Ходит игрок "O"'
        take_input("X", position)
        counter += 1
    else:
        alert_label['text'] = 'Ходит игрок "X"'
        take_input("O", position)
        counter += 1
    if counter == 9 and not (check_win(field)):
        alert_label['text'] = 'Игра окончена. Ничья.'
    elif counter >= 5 and check_win(field):
        alert_label['text'] = f'Игрок "{check_win(field)}" выиграл!'
        # игра окончена, кнопки не нажимаются:
        for button in field:
            button['command'] = ''
        if check_win(field) == 'X':
            winner_x += 1
        else:
            winner_o += 1


def new_game():
    global counter, field
    counter = 0
    field = []
    alert_label['text'] = 'Новая игра'
    label_x['text'] = f'X:{winner_x}'
    label_o['text'] = f'O:{winner_o}'
    make_buttons()


new_game()
form.mainloop()
