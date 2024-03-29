"""
✔ Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для второго ключа.
✔четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
"""


def get_dict_args(s: str) -> dict[int: int | tuple]:
    nums = tuple(s.split('/'))
    return {nums[1]: nums[0], nums[2]: nums[3:]}
