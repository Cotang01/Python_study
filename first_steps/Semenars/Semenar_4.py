# """
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# """
# # Первый метод
#
# stroka = input('Введите текст: ')
# list1 = list(stroka)
# print(list1)
# dict1 = dict()
# for i in set(list1):
#     dict1.setdefault(i, 0)
# print(dict1)
#
# for key, value in dict1.items():
#     for i in range(len(list1)):
#         if list1[i] == key:
#             if value > 0:
#                 list1[i] = f'{key}_{value}'
#             value += 1
#
# stroka_postfixed = ''
# for i in list1:
#     stroka_postfixed += f'{i} '
# print(stroka_postfixed)
#
# # Второй метод
#
# stroka = input('Введите текст: ')
# dict1 = {}
#
# for i in stroka:
#     if i in dict1:
#         print(f'{i}_{dict1[i]}', end=" ")
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
#         print(i, end=" ")
# # Третий метод
#
# import string
# import random
#
# my_string = ''.join([random.choice(string.ascii_letters) for _ in range(30)])
#
# dict_count = {}
# total_string = ''
# for char in my_string:
#     dict_count[char] = dict_count.get(char, 0) + 1
#     if dict_count.get(char, 0) > 1:
#         total_string += (f'{char}_{dict_count.get(char)} ')
#     else:
#         total_string += char + ' '
# print(total_string)
#
# """
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
# """
# # Первый метод
# string1 = input('Введите текст: ')
# words = string1.split()
# words_amount = set()
# index = 0
#
# for i in words:
#     words_amount.add(words[index])
#     index += 1
#
#
# print(f'В введённом тексте {len(words_amount)} различных слов.')
#
# # Второй метод
#
# import string
#
# my_string = input('Введите текст: ')
#
# for char in string.punctuation:
#     my_string.replace(char, ' ')
# my_string = my_string.lower().split()
# print(f'В введённом тексте {len(set(my_string))} различных слов.')
#
# """
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырехзначных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
# """
# import random
#
# list_1 = [random.randint(1000, 9999) for i in range(random.randint(2, 10))]
# print(list_1)
#
# remove_digit = int(input('Введите цифру, которую нужно убрать: '))
#
# for index in range(len(list_1)):
#     if str(remove_digit) in str(list_1[index]):
#         list_1[index] = int(str(list_1[index]).replace(str(remove_digit), ''))
# print(list_1)
#
# # Первый метод
# for index in range(len(list_1)):
#     list_1[index] = (list_1[index] % 10) + (list_1[index] % 100 // 10) + (list_1[index] % 1000 // 100) \
#                     + (list_1[index] // 1000)
#     while list_1[index] >= 10:
#         list_1[index] = (list_1[index] % 10) + (list_1[index] // 10)

# # # Второй метод
# # for i in range(len(list_1)):
# #     while len(str(list_1[i])) > 1:
# #         list_1[i] = str(sum(list(map(int, list_1[i]))))
# print(list_1)
# print(set(list_1))
