"""
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def receive_until_num() -> None:
    try:
        input_ = input('-> ')
        if not isinstance(input_, int) or not isinstance(input_, float):
            raise ValueError('Not number received:', input_)
    except ValueError:
        receive_until_num()
