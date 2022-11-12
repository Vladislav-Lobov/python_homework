# Задача 0002
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#   a) Добавьте игру против бота
#   b) Подумайте как наделить бота "интеллектом"

import random


# искусственный интеллект
def get_AI():
    global all_candies
    global max_for_turn

    # последние выигрышные позиции
    if all_candies in range(1, max_for_turn + 1):
        candies = all_candies
    # отсутствие кратности (max_for_turn + 1) это все выигрышные позиции
    else:
        candies = all_candies % (max_for_turn + 1)
        if candies == 0:
            # все остальные позиции проигрышные
            candies = random.randint(1, max_for_turn)
    return candies


def human_against_human():
    global all_candies
    global max_for_turn

    print('Игрок 1' if (gamer := random.randint(1, 2))
          == 1 else 'Игрок 2', 'ходит первым')

    while all_candies > 0:

        print(f'Осталось {all_candies} конфет. Игрок {gamer} ходит: ')
        while (candies := int(input('Введите количество конфет: '))) < 1 or (candies > max_for_turn):
            print(
                f'Неверный ввод. Количество конфет должно быть от 1 до {max_for_turn}')
        all_candies = all_candies - candies
        (gamer := 2) if gamer == 1 else (gamer := 1)

    print(f'Игра окончена, игрок {gamer} проиграл')


def human_against_bot():
    global all_candies
    global max_for_turn

    print('Вы ходите первым' if (gamer := random.randint(1, 2))
          == 1 else 'Программа ходит первая')

    while all_candies > 0:

        print(f'Осталось {all_candies} конфет.')
        if gamer == 1:
            while (candies := int(input('Введите количество конфет: '))) < 1 or (candies > max_for_turn):
                print(
                    f'Неверный ввод. Количество конфет должно быть от 1 до {max_for_turn}')
        else:
            candies = get_AI()
            print(f'Ход программы: {candies} конфет')

        all_candies = all_candies - candies
        (gamer := 2) if gamer == 1 else (gamer := 1)

    print(f'Игра окончена', 'компьютер' if gamer == 2 else 'Вы', 'в проигрыше')


def bot_against_bot():
    global all_candies
    global max_for_turn

    print('Бот №1 ходит первый' if (gamer := random.randint(1, 2))
          == 1 else 'Бот №2 ходит первый')

    while all_candies > 0:

        print(f'Осталось {all_candies} конфет.')
        if gamer == 1:
            candies = get_AI()
            print(f'Ход бота №1: {candies} конфет')
        else:
            candies = get_AI()
            print(f'Ход бота №2: {candies} конфет')

        all_candies = all_candies - candies
        (gamer := 2) if gamer == 1 else (gamer := 1)

    print(f'Игра окончена', 'Бот №2' if gamer ==
          2 else 'Бот №1', 'в проигрыше')


all_candies = 2021
max_for_turn = 28
human_against_human()


all_candies = 2021
max_for_turn = 28
human_against_bot()

all_candies = 2021
max_for_turn = 28
bot_against_bot()
