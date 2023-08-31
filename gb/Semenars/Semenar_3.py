# ТРЕТИЙ СЕМЕНАР
#
# """
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# """
# import random
#
# list_1 = [random.randint(0, 20) for _ in range(40)]
# print(len(set(list_1))) # set() переводит список в множество, где нет повторяющихся элементов, у set() нет индексов
#
# """
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# """
# import random
# count = 0
# list_len = int(input('Введите длину последовательности: '))
# list_1 = [random.randint(1, 9) for _ in range(list_len)]
# print(list_1)
# k = int(input('На какое количество элементов сдвинуть?: '))
# # Первый метод
# while count < k:
#     list_1.insert(0, list_1.pop())
#     count += 1
# print(list_1)
#
# Второй метод
# for i in range(k):
#     list_1.insert(0, list_1.pop())
# print(list_1)
#
# Третий метод
# print(list_1[-k:] + list_1[:-k])
#
# Четвёртый метод
# for _ in range(k):
#     list_1.insert(0, list_1.pop())
# print(list_1)
#
# Пятый метод
# for i in range(len(list_1)):
#     print(list_1[i - k], end=', ')
#
# """
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# """
# import random
#
# count = 0
# list_1 = [random.randint(0, 10) for _ in range(5)]
# print(list_1)
# Первый метод
# for i in range(1, len(list_1)):
#     if list_1[i-1] < list_1[i]:
#         count += 1
# print(count)
# Второй метод
# list_2 = [i for i in range(1, len(list_1)) if list_1[i-1] < list_1[i]]
# print(len(list_2))
#
# """
# Дана упорядоченная последовательность an чисел от 1 до N.
# Из копии данной последовательности bn удалили одно число, а оставшиеся перемешали.
# Найти удаленное число.
# """
# from random import shuffle
# n = int(input('До какого числа будет идти последовательность?: '))
# an = [_ for _ in range(1, n+1)]
# print(an)
# bn = an.copy()
# n1 = int(input('Какое число удалим?: '))
# # Первый метод
# bn.remove(n1)
# shuffle(bn)
# print(bn)
# set1 = set(an)
# set2 = set(bn)
# print(set1.difference(set2))
# # Второй метод
# list_1 = sum(an)
# list2 = sum(bn)
# print(list_1 - list2)
# import random
# list_1 = [random.randint(0, 10) for _ in range(20)]
# print(list_1)
#
# count_dict = {}
#
# for i in list_1: # Создание словаря, который показывает, сколько каких чисел в списке list_1
#     count_dict[i] = count_dict.get(i, 0) + 1
#
# print(count_dict)
