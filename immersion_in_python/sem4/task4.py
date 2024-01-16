"""
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""


def sort_list(arr: list[int]) -> list[int]:
    """ Merge Sort """
    m = 1
    while m < len(arr):
        j = 0
        while j + m < len(arr):
            bose_nelson_merge(arr, j, m, m)
            j = j + m + m
        m = m + m
    return arr


def bose_nelson_merge(arr, j, r, m):
    if j + r < len(arr):
        if m == 1:
            if arr[j] > arr[j + r]:
                arr[j], arr[j + r] = arr[j + r], arr[j]
        else:
            m = m // 2
            bose_nelson_merge(arr, j, r, m)
            if j + r + m < len(arr):
                bose_nelson_merge(arr, j + m, r, m)
            bose_nelson_merge(arr, j + m, r - m, m)
    return arr


def bubble_sort(arr: list[int]) -> list[int]:
    """ Bubble Sort """
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
