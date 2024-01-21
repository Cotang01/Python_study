"""
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итератор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""

from immersion_in_python.sem5.task2 import get_dict_from_str

my_iterator = iter(get_dict_from_str('hjuihrgihnndf').items())

for i in range(5):
    print(next(my_iterator))
