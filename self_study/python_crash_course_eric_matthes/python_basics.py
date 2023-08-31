# n = int(input('Введите число: '))
#
#
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
#
#
# print(sum_numbers(n))

# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c#',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
#
# for i in favorite_languages.keys():  # Проходится по ключам словаря
#     print(f'{i.title()}')
# for i in favorite_languages.values():  # Проходится по значениям словаря
#     print(f'{i.title()}')
"""
Но значения из словаря извлекаются без проверки на повторения.
Чтобы получить значения без повторений, надо воспользоваться set()
"""
import random

# favorite_languages = {
#   'jen': 'python',
#   'sarah': 'c#',
#   'edward': 'ruby',
#   'phil': 'python',
#   }
#
# for i in set(favorite_languages.values()):  # Проходится по значениям словаря
#     print(f'{i.title()}')

# """
# Словари от множеств отличаются наличием пар 'ключ: значение'
# """

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for i in aliens:
#     print(i)  # Цикл, возвращающий все словари в списке
# print(aliens[0])  # Возвращение первого словаря в списке

#  Создадим 30 словарей и поместим их в список
# aliens = []
# for i in range(30):
#     alien = {'color': 'green', 'points': 5}
#     aliens.append(alien)
# print(f' Всего пришельцев: {len(aliens)}')
# # for i in aliens[:5]:
# #     print(i)
# for alien in aliens[:3]:  # Замена значений словарей в списке через цикл for
#     # и условие if
#     if alien['color'] == 'green':  # Первые 3 словаря в списке меняют
#         # значения внутри себя
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#         print(alien)
# for alien in aliens[:2]:  # Первые 2 словаря в списке меняют значения внутри
#     # себя
#     if alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
#         print(alien)
# Списки в словаре
# pizza = {
#  'crust': 'thick',
#  'toppings': ['mushrooms', 'extra cheese'],
#  }
# print(pizza)
# if 'mushrooms' in pizza['toppings']:
#     print(True)
#
# Словари в словаре
# users = {
#  'aeinstein': {
#      'first': 'albert',
#      'last': 'einstein',
#      'location': 'princeton',
#  },
#
#  'mcurie': {
#      'first': 'marie',
#      'last': 'curie',
#      'location': 'paris',
#  },
#  }
# print(users)
# for username, user_info in users.items():  # username (условно i) в данном
#     # случаи это первый ключ словаря users
#     print(f'\nUsername: {username}')
#     full_name = f"{user_info['first']} {user_info['last']}"  # создаём
#     # переменную, которая состоит из ключей, их значение будет браться из
#     # вложенного словаря (вложенный словарь это значение ключа)
#     location = user_info['location']  # создаём ещё одну переменную (условно
#     # j), которой будет присваиваться значение 3 ключа вложенного словаря
#     print(f'\tFull name: {full_name.title()}')
#     print(f'\tLocation: {location.title()}')
#
# # Простыми словами в данном случае aeinstein и mcurie это i-тое, а first,
# # last и location это j-тое, обращение к которым возвращает их значение

# # Тестовое задание
# me = {'first_name': 'alex',
#       'last_name': 'm',
#       'age': 21,
#       'city': 'Ekb'}
# friend1 = {'first_name': 'dima',
#       'last_name': 'k',
#       'age': 21,
#       'city': 'Ekb'}
# friend2 = {'first_name': 'ilya',
#       'last_name': 's',
#       'age': 22,
#       'city': 'Ekb'}
#
# people = [me, friend1, friend2]
#
# for i in people:
#     print(f'Full name: {i["first_name"].title()} {i["last_name"].title()}')
#     print(f'\tInfo: {i["age"]} \n\tCity: {i["city"]}')
#
# monya = {'specie': 'cat', 'owner': 'alexander'}
# busya = {'specie': 'dog', 'owner': 'alexander'}
#
# pets = [monya, busya]
#
# for i in pets:
#     print(f'\tВид: {i["specie"].title()} \t\nВладелец: {i["owner"].title()}')
#
# favourite_places = {'alex':
#                         {'first': 'home',
#                          'second': 'sauna',
#                          'third': 'park'},
#                     'mama':
#                         {'first': 'home',
#                          'second': 'banya',
#                          'third':'village'},
#                     'friend':
#                         {'first': 'racing track',
#                          'second': 'home',
#                          'third': 'yes'}}
# for i, j in favourite_places.items():
#         print(f'\t\nName: {i.title()}')
#         print(f'\tPlaces: {j["first"].title()}, {j["second"].title()}, '
#               f'{j["third"].title()}')
#
# favourite_digits = {'alex':
#                         {'digits': '13, 69, 228'},
#                     'valera':
#                         {'digits': '54, 69, 228'},
#                     'semen':
#                         {'digits': '69, 69, 228'}}
#
# for i, j in favourite_digits.items():
#     print(f'\nName: {i.title()}')
#     print(f'\tFavourite digits: {j["digits"]}')
#
# cities = {'Ekb':
#               {'country': 'Russia',
#                'population': '1.5 mil',
#                'fact': 'normal city'},
#           'Piter':
#               {'country': 'Russia',
#                'population': '5.5 mil',
#                'fact': 'solevoy'},
#           'Moscow':
#               {'country': 'Russia',
#                'population': '13 mil',
#                'fact': 'burzhui'}
#           }
# for key, value in cities.items():
#     print(f'\nCity: {key.title()}')
#     print(f'\tCountry: {value["country"]} '  # Можно уместить в 1 команде
#           f'\n\tPopulation: {value["population"]} '
#           f'\n\tFact: {value["fact"].title()}')
#     print(f'\tPopulation: {value["population"]}')
#     print(f'\tFact: {value["fact"].title()}')
#
# Ввод данных
# your_name = 'Привет, это тестовая программа.'
# your_name += '\nКак тебя зовут? '
#
# name = input(your_name)
# print(f'Привет, {name}!')
#
# Ввод данных и оператор вычисления остатка %
# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print('Это число чётное')
# else:
#     print('Это число нечётное')
# ordered_tables = int(input('Сколько столиков вы хотите заказать? '))
# if ordered_tables > 8:
#     print('Такого количества у нас в доступе нет :(')
# else:
#     print('Заказ принят!')
# number_10 = int(input('Введите число: '))
# if number_10 % 10 == 0:
#     print('Это число кратно 10.')
# else:
#     print('Это число не кратно 10, фальшивка')
#
# Прерывание работы программы используя цикл while
# prompt = '\nНапиши Выход: '
# message = ''
# while message.upper() != 'ВЫХОД':
#     message = input(prompt)
#     if message.upper() == 'ВЫХОД':
#         print('Ок')
#
# Флаги
# prompt = '\nНапиши Выход: '
# flag1 = True
# while flag1:
#     message = input(prompt)
#     if message.upper() == 'ВЫХОД':
#         flag1 = False
#     else:
#         message
# if flag1 == False:
#     print('Ты справился')
#

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# list2 = []
#
# for i in list1:
#     if i % 2 == 0:
#         list2.append((i, i**2))
#
# print(list1)
# print(list2)

# string = str(input('Введите набор чисел через пробел: '))
# print(string)
# string = list(map(int, string.split()))  # преобразуем строку в список,
# # применяем int функцией map. list здесь это то, что будет в итоге
# print(string)

# print(string.split())  # .split() преобразует строку в список,
# # разделителем изначально считается пробел
# list1 = []
# for i in string:
#     if i.isdigit():
#         list1.append(int(i))
# print(list1)

# list_1 = [random.randint(1, 20) for i in range(20)]
# print(list_1)
# list_2 = list(filter(lambda x: x % 10 == 5, list_1))
# print(list_2)

# Функция zip() проходится по самому наименьшему списку и возвращает
# кортежи, (в случае со словарями, возвращает пары ключ-значение)
# list_1 = [1, 2, 3, 4, 5, 6]
# list_2 = [10, 20, 30, 40, 50, 60, 70, 80]
# result_1 = list(zip(list_2, list_1))
# result_2 = dict(zip(list_2, list_1))  # Если мы на выходе создаём словарь,
# то элементы первого списка будут ключами, а элементы второго списка - их
# значениями
# print(result_1)
# print(result_2)

# Функция enumerate() проходится по списку и возвращает кортежи, первым
# значением которых будет присвоенный номер (от 0), а вторым -
# соответствующий элемент списка
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
# for i in enumerate(numbers, 1):  # Начинает отсчёт с 1, а не с 0
#     print(i)

# Функция map применяет другую функцию ко всем элементам списка
# numbers = '123456789'
# numbers = list(numbers)
# print(numbers)
#
# numbers = list(map(int, numbers))
# print(numbers)
#
# numbers = list(map(lambda x: x + 1, numbers))
# print(numbers)
#
# numbers = list(map(lambda x: x**2, numbers))
# print(numbers)

# Функция filter отсеивает элементы на основании функции
# numbers = '123456789'
# numbers = list(map(int, numbers))
# print(numbers)
#
# numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(numbers)

# Функция lambda это анонимная функция, которая всегда что-то возвращает.
# Lambda применяется тогда, когда надо что-то быстро выполнить 1 раз и если
# к ней больше не потребуется обращаться
# print((lambda x, y, z: x + y + z)(1, 2, 3))
