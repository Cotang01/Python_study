"""
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
from task2 import get_json_data
import csv


def convert_json_to_csv(file_path: str, csv_file: str) -> None:
    json_data = get_json_data(file_path)
    with open(csv_file, mode='w', encoding='UTF-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(('Level', 'ID', 'Name'))

        for lvl, persons in json_data.items():
            for pid, name in persons.items():
                csv_writer.writerow([lvl, pid, name])

