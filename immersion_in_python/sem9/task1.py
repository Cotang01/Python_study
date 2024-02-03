"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""


def start_guess_game():
    number, tries = map(int, input('Загадайте число от 1 до 100 и число '
                                   'попыток от 1 до 10, введите их через '
                                   'пробел\n-> ').split())
    if not 1 <= number <= 100 or not 1 <= tries <= 10:
        print('Попробуйте ещё раз')
        start_guess_game()

    def receive_guess():
        nonlocal number, tries
        cur_try = 0
        while cur_try < tries and int(input(
                f'Попробуйте угадать число, у вас осталось '
                f'{tries - cur_try} попыток\n-> ')) != number:
            cur_try += 1
            print('Не угадал')
        if cur_try == tries:
            print('У вас закончились попытки')
        else:
            print('Угадал!')

    return receive_guess()
