"""
Задача
Написать скрипт в любой парадигме, который выводит на экран таблицу
умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм.
"""

n = int(input("Введите число: "))
for i in range(1, n + 1):
    print()
    for j in range(1, n + 1):
        print(f'{i} * {j} = {i * j}', end='; ')

"""
Для решения задачи была выбрана структурная парадигма программирования,
потому что это позволило решить задачу быстрее, чем если бы использовалась
другая парадигма.
"""
