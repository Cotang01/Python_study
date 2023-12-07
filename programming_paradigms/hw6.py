"""
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.
"""


class Solution:
    def binary_search(self, arr: list[int], target) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] > target:
                right = middle - 1
            elif arr[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1
