"""
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import pickle
import os
from task2 import get_json_data


def json_to_pickle(dir_path: str = '.') -> None:
    json_files = list_json_files(dir_path)
    for file_path in json_files:
        full_path = file_path.split(os.sep)
        file_name = full_path[-1]
        new_name = file_name.replace('json', 'pkl')
        new_path = os.sep.join(full_path[:-1] + [new_name])
        with open(file_path, 'r', encoding='UTF-8') as file:
            file_data = get_json_data(file_path)
        with open(new_path, 'wb') as pkl_file:
            pickle.dump(file_data, pkl_file)


def list_json_files(dir_path: str) -> list[str]:
    return [os.path.abspath(f) for f in os.listdir(dir_path)
            if f.split('.')[-1] == 'json']
