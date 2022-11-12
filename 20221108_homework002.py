# Задача 002
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых  и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и  [1, 3, 5] и [1, 2, 5, 3, 10]


import random

array = [random.randint(1, 10) for i in range(10)]
array.sort()

print(f'Исходный случайный массив: {array}')
descent = set(array)
print(f'Последовательность без дубликатов: {descent}')
duplicate = set([i for i in descent if array.count(i) > 1])
print(f'Список из повторяющихся элементов {duplicate}')
unique = descent - duplicate
print(f'Список уникальных элементов {unique}')
