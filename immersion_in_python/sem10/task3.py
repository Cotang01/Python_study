"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class PersonData:
    """Class for containing info about certain person"""
    def __init__(self, fname: str, sname: str, patronymic: str, _age: int):
        self.fname = fname
        self.sname = sname
        self.patronymic = patronymic
        self._age = _age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f"First name: {self.fname}\n " \
               f"Second name: {self.sname} \n" \
               f"Patronymic: {self.patronymic}\n" \
               f"Age: {self._age}"


print()