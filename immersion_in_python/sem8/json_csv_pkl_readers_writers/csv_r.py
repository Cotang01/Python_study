import csv

__all__ = ['get_csv_data']


def get_csv_data(csv_file):
    with open(csv_file, mode='r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        reader.__next__()
        return [row for row in reader]
