"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны
[1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""


def guess_game_decorator(func: callable):
    def wrapper():
        number, tries = get_num_tries()
        func(number, tries)
    return wrapper


def get_num_tries():
    number, tries = map(int, input('Загадайте число от 1 до 100 и число '
                                   'попыток от 1 до 10, введите их через '
                                   'пробел\n-> ').split())
    if not 1 <= number <= 100 or not 1 <= tries <= 10:
        print('Попробуйте ещё раз')
        get_num_tries()
    return number, tries


@guess_game_decorator
def receive_guess(number: int, tries: int):
    cur_try = 0
    while cur_try < tries and int(input(
            f'Попробуйте угадать число, у вас осталось '
            f'{tries - cur_try} попыток\n-> ')) != number:
        cur_try += 1
        print('Не угадал')
    if cur_try > tries:
        print('У вас закончились попытки')
    else:
        print('Угадал!')
