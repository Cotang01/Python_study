"""
� Добавьте в модуль с загадками функцию, которая
принимает на вход строку (текст загадки) и число (номер
попытки, с которой она угадана).
� Функция формирует словарь с информацией о результатах
отгадывания.
� Для хранения используйте защищённый словарь уровня
модуля.
� Отдельно напишите функцию, которая выводит результаты
угадывания из защищённого словаря в удобном для чтения
виде.
� Для формирования результатов используйте генераторное
выражение.
"""

__all__ = ['print_quiz_results']


# from task4.py
def quiz_game(riddle: str, answers: list[str], tries: int) -> int:
    print(riddle)
    ans = set(answers)
    for t in range(1, tries + 1):
        if input('-> ').lower() in ans:
            return t
    return 0


# from task5.py
def riddles():
    data = {'В Полотняной стране\n'
            'По реке Простыне\n'
            'Плывет пароход\n'
            'То назад, то вперед,\n'
            'А за ним такая гладь —\n'
            'Ни морщинки не видать.': ['утюг'],
            'Стоит дуб. В нём 12 гнёзд. В каждом гнезде по 4 яйца, '
            'в каждом яйце по 7 цыплят.': ['год']}

    return [(rid, quiz_game(rid, ans, 3)) for rid, ans in data.items()]


def get_quiz_results() -> dict:
    return {res[0]: res[-1] for res in riddles()}


def print_quiz_results():
    for rid, tr in get_quiz_results().items():
        tr = f'Была отгадана за {tr} попыток' if tr else 'Не была отгадана'
        print(f'\t\tЗагадка v\n{rid}\n\t{tr}')
        print()
