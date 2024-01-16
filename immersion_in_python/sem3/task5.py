"""
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""
import random

data = [random.randint(0, 10) for _ in range(25)]
print(data)

res = [i+1 for i in range(len(data)) if data[i] % 2 != 0]
print(res)
