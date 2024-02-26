"""
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
from string import ascii_letters


def keep_latin_and_spaces(s: str) -> str:
    """
    A function that returns str obj in lower case that only contains latin
    letters and spaces from str s.
    >>> keep_latin_and_spaces('hello')
    'hello'
    >>> keep_latin_and_spaces('HELLO')
    'hello'
    >>> keep_latin_and_spaces('hello, world!')
    'hello world'
    >>> keep_latin_and_spaces('Привет')
    ''
    >>> keep_latin_and_spaces('Привет, User!')
    ' user'
    """
    letters = set(ascii_letters + ' ')
    return ''.join(filter(lambda x: x in letters, s)).lower()
