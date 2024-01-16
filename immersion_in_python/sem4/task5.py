"""
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""


def get_workers_pay(
        names: list[str],
        salaries: list[int],
        bonuses: list[str]) -> dict[str: float]:
    return {names[i]: salaries[i] + salaries[i] * (float(bonuses[i][:-1])/100)
            for i in range(len(names))}
