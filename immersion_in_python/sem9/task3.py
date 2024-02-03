"""
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""
import json


def save_params_res_to_json(func: callable):
    def wrapper(**kwargs):
        res = func(**kwargs)
        with open(f'{func.__name__}.json', 'a', encoding='UTF-8') as json_file:
            data = {k: v for k, v in kwargs.items()}
            data['Result'] = res
            json.dump(data, json_file)
        return res
    return wrapper


@save_params_res_to_json
def bar(a: int, b: int):
    return a + b
