# """
# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# """
#
# element_1st = int(input('Введите первый элемент: '))
# element_diff = int(input('Введите разность элементов: '))
# element_len = int(input('Введите длину прогрессии: '))
# progression = [element_1st]
# index = 0
#
# for i in range(element_len - 1):
#     progression.append(progression[index] + element_diff)
#     index += 1
#
# print(progression)
#
# """
# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# """
# import random
#
# list_1_len = int(input('Введите длину списка: '))
# list_1 = [random.randint(1, 20) for _ in range(list_1_len)]
# print(list_1)
# selected_range_start = int(input('Введите начало диапазона: '))
# selected_range_end = int(input('Введите конец диапазона: '))
# list_ranged = []
# index = 0
#
# for i in range(len(list_1)):
#     if selected_range_start <= list_1[index] <= selected_range_end:
#         list_ranged.append(list_1[index])
#     index += 1
#
# print(f'Значения, принадлежащие заданному диапазону: {list_ranged}')
#