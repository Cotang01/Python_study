"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
from task3 import PersonData


class WorkerData(PersonData):
    """Class for containing info about worker"""
    def __init__(self,
                 fname: str,
                 sname: str,
                 patronymic: str,
                 _age: int,
                 pid: int):
        super().__init__(fname, sname, patronymic, _age)
        if not len(str(pid)) == 6:
            raise ValueError("Personal ID is not six-digit")
        else:
            self.pid = pid
            self.level = sum(map(int, str(pid))) % 7
