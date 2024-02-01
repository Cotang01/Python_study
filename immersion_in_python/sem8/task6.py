"""
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестирования возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import pickle
import csv


def pkl_to_csv(pkl_file: str, csv_file: str):
    data_from_pkl = get_pickle_data(pkl_file)
    with open(csv_file, 'w', newline='', encoding='UTF-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Level', 'ID', 'Name', 'Hash'])
        for lvl, person in data_from_pkl.items():
            for pid, data in person.items():
                csv_writer.writerow([lvl, pid, data[0], data[1]])


def get_pickle_data(file_path: str):
    with open(file_path, 'rb') as pkl_file:
        return pickle.load(pkl_file)
