"""
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
from random import randint, uniform


def fill_with_nums(file_name: str, pair_nums: int) -> None:
    with open(file_name, mode='w', encoding='UTF-8') as file:
        for _ in range(pair_nums):
            file.write(f'{randint(-1000, 1000)}|{uniform(-1000, 1000)}\n')
