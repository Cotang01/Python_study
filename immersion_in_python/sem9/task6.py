"""
Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""
from functools import wraps
import json


def repeat(num: int):
    def decorator(func: callable):
        @wraps(func)
        def wrapper(**kwargs):
            for _ in range(num):
                number, tries = map(int, input(
                    'Загадайте число от 1 до 100 и число '
                    'попыток от 1 до 10, введите их через '
                    'пробел\n-> ').split())
                while not 1 <= number <= 100 or not 1 <= tries <= 10:
                    number, tries = map(int, input(
                        'Попробуйте ещё раз\n-> '))
                res = func(number=number, tries=tries)
                with open(f'{func.__name__}.json', 'a',
                          encoding='UTF-8') as json_file:
                    data = {k: v for k, v in kwargs.items()}
                    data['Result'] = res
                    json.dump(data, json_file)
        return wrapper
    return decorator


@repeat(2)
def receive_guess(number: int, tries: int):
    """Docstring"""
    cur_try = 0
    while cur_try < tries and int(input(
            f'Попробуйте угадать число, у вас осталось '
            f'{tries - cur_try} попыток\n-> ')) != number:
        cur_try += 1
        print('Не угадал')
    if cur_try == tries:
        print('У вас закончились попытки')
        return -1
    else:
        print('Угадал!')
    return 1
