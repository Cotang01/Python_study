"""
� Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную
защищённую функцию.
"""
from datetime import date
from calendar import isleap


__all__ = ['is_real_date', 'is_leap_year']


def is_real_date(date_: str) -> bool:
    try:
        d, m, y = date_.split('.')
        date.fromisoformat(f'{y}-{m.zfill(2)}-{d.zfill(2)}')
        return True
    except ValueError:
        return False


def is_leap_year(year: int):
    return isleap(year) or year == 1582
