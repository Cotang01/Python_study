"""
� Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
"""
from random import randint


def gamble_game(low: int, top: int, tries: int) -> bool:
    rng_num = randint(low, top)
    for _ in range(tries):
        guess = int(input('-> '))
        if guess == rng_num:
            return True
        elif guess > rng_num:
            print('Меньше')
        else:
            print('Больше')
    return False
