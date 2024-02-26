"""
Доработайте классы исключения так, чтобы они выдали
подробную информацию об ошибках.
Передавайте необходимые данные из основного кода
проекта.
"""

from typing import List
import json


class LevelError(Exception):
    def __init__(self, cur_level, target_level):
        self.cur_level = cur_level
        self.target_level = target_level

    def __str__(self):
        return f'Current level {self.cur_level} is lower than ' \
               f'{self.target_level}'


class PermissionException(Exception):
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid

    def __str__(self):
        return f'User with name {self.name} and id {self.pid} does not exists'


class LoginSystem:

    def __init__(self, file_path):
        self.data = self.gen_users_from_json(file_path)
        self.logged_level = None

    def login(self, name, pid) -> int:
        for user in self.data:
            if user.name == name and user.pid == pid:
                self.logged_level = user.level
                return user.level
        raise PermissionException(name, pid)

    def register(self, name, pid, level) -> None:
        if not self.logged_level or level > self.logged_level:
            raise LevelError(self.logged_level, level)
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
