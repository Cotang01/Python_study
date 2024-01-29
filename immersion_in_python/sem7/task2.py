"""
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
import string
from random import randint


def gen_nicknames(count: int) -> None:
    letters = string.ascii_letters[:26]
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    with open('task2.txt', mode='a', encoding='UTF-8') as file:
        for _ in range(count):
            valid = False
            while not valid:
                name = ''.join([letters[randint(0, 25)]
                                for _ in range(randint(4, 7))])
                for ch in name:
                    if ch in vowels:
                        valid = True
            file.write(f'{name.capitalize()}\n')
