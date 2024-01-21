"""
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def is_prime(num: int) -> bool:
    for div in range(3, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True


def primes_generator(n: int) -> int:
    for num in range(3, n, 2):
        if is_prime(num):
            yield num


for i in primes_generator(int(input('-> '))):
    print(i)
