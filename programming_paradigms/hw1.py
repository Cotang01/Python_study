"""
Задача №1
Дан список целых чисел numbers. Необходимо написать в императивном стиле
процедуру для сортировки числа в списке в порядке убывания. Можно использовать
любой алгоритм сортировки.
Задача №2
Написать точно такую же процедуру, но в декларативном стиле
"""


class Solution:
    """
    Класс решения.
    """
    def sort_list_imperative(self, numbers: list[int]) -> list[int]:
        """
        Алгоритм сортировки списка целых чисел в императивном стиле.
        Поразрядная сортировка.
        :param numbers: список целых чисел.
        :return: отсортированный список целых чисел.
        """
        max_num = numbers[0]
        for index in range(1, len(numbers)):
            if numbers[index] > max_num:
                max_num = numbers[index]
        max_radix = len(str(max_num))
        buckets = [[] for _ in range(10)]
        for i in range(max_radix):
            for num in numbers:
                cur_radix = (num // 10 ** i) % 10
                buckets[cur_radix].append(num)
            numbers = [num for bucket in buckets for num in bucket]
            buckets = [[] for _ in range(10)]
        return list(reversed(numbers))

    def sort_list_declarative(self, numbers: list[int]) -> list[int]:
        """
        Алгоритм сортировки списка целых чисел в декларативном стиле.
        Встроенная быстрая сортировка.
        :param numbers: список целых чисел.
        :return: отсортированный список целых чисел.
        """
        numbers.sort(reverse=True)
        return numbers


assert Solution().sort_list_imperative(
    [5, 2, 3213, 525278, 123, 24]) == [525278, 3213, 123, 24, 5, 2]
assert Solution().sort_list_declarative(
    [5, 2, 3213, 525278, 123, 24]) == [525278, 3213, 123, 24, 5, 2]
