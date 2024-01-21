"""
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
"""


def print_fizz_buzz_nums() -> int | str:
    fizz_buzz_dict = {3: 'Fizz', 5: 'Buzz'}
    for num in range(1, 100):
        buffer = ''
        for k, v in fizz_buzz_dict.items():
            if num % k == 0:
                buffer += v
        yield num if not buffer else buffer


for i in print_fizz_buzz_nums():
    print(i)
