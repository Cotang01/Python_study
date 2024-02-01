"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
"""
from task4 import get_csv_data
import pickle as pkl


def print_pkl_data_from_csv(csv_file: str) -> None:
    print(pkl.dumps(get_csv_data(csv_file)))
