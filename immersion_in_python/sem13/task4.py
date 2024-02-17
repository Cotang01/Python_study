"""
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""
from typing import List
import json


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


def get_json_data(file_path: str) -> dict:
    try:
        with open(file_path, mode='r', encoding='UTF-8') as file:
            return json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        print("File is empty, file not found or data type doesn't match JSON")
        return {}


def gen_users_from_json(file_path: str) -> List[User]:
    return [User(n, int(p), int(l))
            for l, inner in get_json_data(file_path).items()
            for (p, n) in inner.items()]
