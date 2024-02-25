"""
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)

вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.

добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""
from typing import List
import json
from task3 import LevelError, PermissionException


class LoginSystem:

    def __init__(self, file_path):
        self.data = self.gen_users_from_json(file_path)
        self.logged_level = 0

    def login(self, name, pid) -> int:
        for user in self.data:
            if user.name == name and user.pid == pid:
                self.logged_level = user.level
                return user.level
        raise PermissionException('invalid user data')

    def register(self, name, pid, level) -> None:
        if level < self.logged_level:
            raise LevelError('Greater level not allowed')
        self.data.append(User(name, pid, level))

    @staticmethod
    def _get_json_data(file_path: str) -> dict:
        try:
            with open(file_path, mode='r', encoding='UTF-8') as file:
                return json.load(file)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            print(
                "File is empty, file not found or data type doesn't match JSON")
            return {}

    def gen_users_from_json(self, file_path: str) -> List:
        return [User(n, int(p), int(l))
                for l, inner in self._get_json_data(file_path).items()
                for (p, n) in inner.items()]


class NameDesc:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class PidDesc:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class LevelDesc:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class User:
    name = NameDesc()
    pid = PidDesc()
    level = LevelDesc()

    def __init__(self, name, pid, level):
        self.name = name
        self.pid = pid
        self.level = level

    def __str__(self):
        return f'{self.__class__.__name__}' \
               f'{tuple(vars(self).values())}'

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'{tuple(vars(self).values())}'

    def __eq__(self, other):
        return self.name == other.name and self.pid == other.pid
