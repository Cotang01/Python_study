"""
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""


def are_profitable(companies: dict[str: list[tuple[int, int]]]) -> bool:
    for v in companies.values():
        profit = 0
        for pair in v:
            profit += pair[0] - pair[-1]
        if profit < 0:
            return False
    return True
