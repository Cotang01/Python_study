"""
� Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
� Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны.
"""


def quiz_game(riddle: str, answers: list[str], tries: int) -> int:
    print(riddle)
    ans = {an.lower() for an in answers}
    for t in range(tries):
        if input('-> ').lower() in ans:
            return t + 1
    return 0
