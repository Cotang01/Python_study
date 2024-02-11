"""
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


class Archive:
    """Class with archived attr values of previous instances"""
    nums_archive = []
    strings_archive = []

    def __init__(self, number: int, string: str):
        self.number = number
        self.string = string
        self.nums_archive.append(number)
        self.strings_archive.append(string)

    def __str__(self):
        return f"Values: {self.number}, {self.string}\n" \
               f"Storage: {self.nums_archive}, {self.strings_archive}"

    def __repr__(self):
        return str(self.number), str(self.string), \
               str(self.nums_archive), str(self.strings_archive)
