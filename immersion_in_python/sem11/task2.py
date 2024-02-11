"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
"""


class Archive:
    nums_archive = []
    strings_archive = []

    def __init__(self, number: int, string: str):
        self.number = number
        self.string = string
        self.nums_archive.append(number)
        self.strings_archive.append(string)
