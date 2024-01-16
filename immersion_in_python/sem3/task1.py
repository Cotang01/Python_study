"""
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
"""
import random

data = [random.randint(0, 10) for _ in range(10)]


def remove_doubles_imp(arr: list[int]) -> list[int]:
    return list(set(arr))


def remove_doubles_dec(arr: list[int]) -> list[int]:
    arr.sort()
    # Обход в обратную сторону
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == arr[i-1]:
            arr.remove(arr[i])
    return arr
