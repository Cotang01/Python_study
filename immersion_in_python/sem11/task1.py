"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""
from time import localtime


class MyString(str):
    def __init__(self, string: str, author: str = ''):
        super().__init__(string)
        self.author = author
        self.creation_time = localtime()
