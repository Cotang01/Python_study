"""
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""
import json
from typing import Dict, List


class Factorial:
    """Class for storing number and k last values of its factorial sequence"""
    def __init__(self, k, file_name: str = 'factorial.json'):
        self.k: int = k
        self.prevs: Dict[int: List[int]] = {}
        self.file_name = file_name

    def __call__(self, n):
        vals = [1]
        vals = [vals[-1] for i in range(1, n + 1)
                if not vals.append(i * vals[-1])][-self.k:]
        self.prevs[n] = vals
        return vals

    def show_prevs(self):
        return self.prevs

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_name, 'w', encoding='UTF-8') as js_file:
            json.dump(self.prevs, js_file)
