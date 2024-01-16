"""
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""


def convert(inp: str):
    try:
        inp = int(inp)
        inp = float(inp)
        inp = -inp
    except ValueError:
        pass
    if isinstance(inp, str):
        if inp.lower() != inp:
            inp = inp.lower()
        else:
            inp = inp.lower()  # ???
    return inp


print(convert(input('-> ')))
