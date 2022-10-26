# Задача 0003
# Создайте программу для игры в "Крестики-нолики".

gameplace = ['*'] * 9


def print_gameplace(gameplace):
    print("-------------")
    for i in range(3):
        print("|", gameplace[0+i*3], "|",
              gameplace[1+i*3], "|", gameplace[2+i*3], "|")
        print("-------------")


def take_input(X_or_O):
    is_correct = False
    while not is_correct:
        player_answer = input(f"Куда поставим {X_or_O} ? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный символ... ")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(gameplace[player_answer-1]) not in "XO"):
                gameplace[player_answer-1] = X_or_O
                is_correct = True
            else:
                print("Клеточка уже занята. Повторите ввод:")
        else:
            print("Некорректный ввод. Введите число от 1 до 9")


def check_win(gameplace):
    win_coord = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for each in win_coord:
        if gameplace[each[0]] == gameplace[each[1]] == gameplace[each[2]] != '*':
            return gameplace[each[0]]
    return False


counter = 0
win = False
while not win:
    print_gameplace(gameplace)
    if counter % 2 == 0:
        take_input("X")
    else:
        take_input("O")
    counter += 1
    if counter == 9 and not(check_win(gameplace)):
        print_gameplace(gameplace)
        print("Ничья!")
        win = True
    elif counter >= 5 and check_win(gameplace):
        print_gameplace(gameplace)
        print(f'{check_win(gameplace)} "выиграл!')
        win = True
