"""
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
"""
from typing import Dict, List


class Factorial:
    """Class for storing number and k last values of its factorial sequence"""
    def __init__(self, k):
        self.k: int = k
        self.prevs: Dict[int: List[int]] = {}

    def __call__(self, n):
        vals = [1]
        vals = [vals[-1] for i in range(2, n + 1)
                if not vals.append(i * vals[-1])][-self.k:]
        self.prevs[n] = vals
        return vals

    def show_prevs(self):
        return self.prevs
