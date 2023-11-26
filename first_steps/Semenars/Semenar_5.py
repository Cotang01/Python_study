# def list_summ(numb: int):
#     if numb == 0:
#         return numb
#     return numb + list_summ(numb-1)
#
# print(list_summ(5))
#
# """
# Последовательностью Фибоначчи называется последовательность чисел a0, a1,
# ..., an, ..., где
# """
#
# def fib(numb):
#     if numb == 0:
#         return 0
#     elif numb == 1:
#         return 1
#     return fib(numb - 1) + fib(numb - 2)
# print(fib(10))
#
# Рекурсией пользоваться можно, но не нужно
#
# def function(num: int) -> int:  # : int - вводимое значение, -> int -
#     # присваиваемое значение на выходе
#     return(num + 1)
#
# """
# Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым
# """
#
# # Немного криво работает
# num = int(input('Введите число: '))
#
#
# def simple_number(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return('Непростое')
#         return('Простое')
#
#
# print(simple_number(num))
#
# import time
# import math
#
# num = int(input('Введите число: '))
#
#
# def simple(_num: int) -> bool:
#     if num in [1, 2, 3]:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(num))):
#         if num % i == 0:
#             return False
#     return True
#
#
# print(simple(num))
#
# def is_simple(num: int) -> bool:
#     for i in range(2, num):
#         if not num%i:
#             return False
#     return True
#
# start = time.time()
# print(simple(num))
# finish = time.time()
#
# print(finish - start)
#
# start = time.time()
# print(is_simple(num))
# finish = time.time()
#
# print(finish - start)
