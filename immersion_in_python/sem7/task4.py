"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""
import string
from random import randint
import os


def gen_files(mask: str,
              name_min_len: int = 6,
              name_max_len: int = 20,
              min_bytes: int = 256,
              max_bytes: int = 4096,
              files_count: int = 42) -> None:
    for _ in range(files_count):
        name = gen_file_name(mask, name_min_len, name_max_len)
        with open(name + '.' + mask, mode='a', encoding='UTF-8') as file:
            file.write(str(bytes(randint(0, 255)
                                 for _ in range(randint(min_bytes, max_bytes)))))


def gen_file_name(mask: str, min_len: int, max_len: int) -> str:
    letters = string.ascii_letters
    name = ''.join([letters[randint(0, 51)]
                    for _ in range(randint(min_len, max_len))])
    if os.path.exists(name):
        gen_file_name(mask, min_len, max_len)
    return name
