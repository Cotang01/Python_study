"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""
import csv
from task2 import write_json_data


def csv_to_json_modified(csv_file: str, json_file: str) -> None:
    data = [[r[0], r[1].zfill(10), r[2].lower(), hash(r[1] + r[2])]
            for r in get_csv_data(csv_file)]
    json_data = {}
    for r in data:
        lvl = r[0]
        pid = r[1]
        name = r[2]
        hsh = r[3]
        if lvl not in json_data:
            json_data[lvl] = {}
        json_data[lvl].update({pid: (name, hsh)})
    write_json_data(json_file, json_data)


def get_csv_data(csv_file):
    with open(csv_file, mode='r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        reader.__next__()
        return [row for row in reader]
