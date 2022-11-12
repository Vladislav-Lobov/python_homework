# Задача 001
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#  Пример:
#  2+2 => 4;
#  1+2*3 => 7;
#  1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
#  Пример:
#  1+2*3 => 7;
#  (1+2)*3 => 9

import sys
import re

PRECEDENCE = {
    '^': 4,  # высший приоритет
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1,
}


def string_to_polish(expr):
    # использование регулярного выражения позволяет работать с двузначными, трехзначными и т.д. целыми числами
    tokens = re.findall(r"(\d+|[\(\)\^\+\*\-\/])", expr)

    stack = []
    postfix = []

    for token in tokens:
        if token.isdigit():
            postfix.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            top = stack.pop()
            while top != '(':
                postfix.append(top)
                top = stack.pop()

        else:
            while stack and (PRECEDENCE[stack[-1]] >= PRECEDENCE[token]):
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())
    return ' '.join(postfix)


OPERATORS = {'+': lambda x, y: x + y, '-': lambda x, y: x -
             y, '*': lambda x, y: x * y, '/': lambda x, y: x // y}


def exec_from_polish(srt):
    stack = []
    srt = srt.split(' ')
    for i in srt:
        if i.isdigit():
            stack.append(i)

        else:
            try:
                cnt1, cnt2 = stack.pop(), stack.pop()
                stack.append(OPERATORS[i](int(cnt2), int(cnt1)))
            except:
                print('Некорректный ввод...')
                sys.exit()

    return stack.pop()


print('Внимание! Программа работает только с целыми числами')
input_string = input('Введите математическое выражение: ')
polish_view = string_to_polish(input_string)
print(f'Ваше выражение в виде обратной польской записи: {polish_view}')
print(f'Полученное значение: {exec_from_polish(polish_view)}')
