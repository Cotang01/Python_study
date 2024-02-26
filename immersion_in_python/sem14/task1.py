"""
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
from string import ascii_letters


def keep_latin_and_spaces(s: str) -> str:
    """
    A function that returns str obj that contains only latin letters and
    spaces from str s.
    """
    letters = set(ascii_letters + ' ')
    return ''.join(filter(lambda x: x in letters, s)).lower()
