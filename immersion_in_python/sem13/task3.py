"""
Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class LevelError(Exception):
    pass


class PermissionException(Exception):
    pass

