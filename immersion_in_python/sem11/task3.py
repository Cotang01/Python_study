"""
Добавьте к задачам 1 и 2 строки документации для классов.
"""
from time import localtime


class MyString(str):
    """Class for custom str object, additionally
    contains author and time of creation"""
    def __init__(self, string: str, author: str = ''):
        super().__init__(string)
        self.author = author
        self.creation_time = localtime()


class Archive:
    """Class with archived attr values of previous instances"""
    nums_archive = []
    strings_archive = []

    def __init__(self, number: int, string: str):
        self.number = number
        self.string = string
        self.nums_archive.append(number)
        self.strings_archive.append(string)
