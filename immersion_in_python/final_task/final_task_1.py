"""
1. Взять класс студент из дз 12-го семинара, добавить запуск из командной
строки(передача в качестве аргумента название csv-файла с предметами),
логирование и написать 3-5 тестов с использованием pytest.
"""
import argparse
# 1
import csv
import logging
from functools import wraps
import pytest


class FullName:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) \
                or any([c.isdigit() for c in value]) \
                or sum([n.istitle() for n in value.split()]) != 2:
            pass
        else:
            setattr(instance, self.name, value)


class CsvData:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        with open(getattr(instance, self.name), 'r', encoding='UTF-8') as f:
            return {k: ([], []) for k in [*csv.reader(f)][0]}

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.split('.')[-1] == 'csv':
            raise ValueError('invalid file name')
        setattr(instance, self.name, value)


class Student:
    full_name = FullName()
    subjects = CsvData()

    def __init__(self, name, csv_file, e_logger):
        self._full_name = name
        self._subjects = csv_file
        self.grades = self.subjects.copy()

        self.add_grade = self._ve_log_decor(self.add_grade, e_logger)
        self.add_test_score = self._ve_log_decor(self.add_test_score, e_logger)

    @staticmethod
    def _ve_log_decor(func, lgr):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as ve:
                lgr.warning(
                    f'{ve}! Func: {func}, args: {args, kwargs}')

        return wrapper

    def add_grade(self, subject, mark):
        if subject not in self.grades:
            raise ValueError(f'Предмет {subject} не найден')
        if not isinstance(mark, int) or not 2 <= mark <= 5:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        else:
            self.grades[subject][0].append(mark)

    def add_test_score(self, subject, test_score):
        if subject not in self.grades:
            raise ValueError(f'Предмет {subject} не найден')
        if not isinstance(test_score, int) or not 0 <= test_score <= 100:
            raise ValueError(f'Оценка должна быть целым числом от 0 до 100')
        else:
            self.grades[subject][1].append(test_score)

    def get_average_grade(self):
        all_grades = [*filter(lambda x: x.isdigit(),
                              str([m for s, (m, t)
                                   in self.grades.items() if m or t]))]
        return sum(map(int, all_grades)) / len(all_grades)

    def get_average_test_score(self, subject):
        all_test_scores = [[n for s, (m, t) in self.grades.items()
                            for n in t if s == subject]]
        return sum(*all_test_scores) / len(all_test_scores[0])

    def __str__(self):
        return f'Студент: {self.full_name}\n' \
               f'Предметы: ' \
               f'{", ".join([s for s, (m, t) in self.grades.items() if m or t])}'


if __name__ == '__main__':
    logger = logging.getLogger(logging.basicConfig(
        filename='subjects.log', filemode='a',
        format='%(asctime)s %(levelname)s %(message)s'))

    parser = argparse.ArgumentParser(description='Command line args parser')
    parser.add_argument('file_name', default='subjects.csv',
                        help="csv file name with student's subjects")
    line_args = parser.parse_args()

    s = Student('Петров', line_args.file_name, logger)
    print(s)


class TestStudent:

    @pytest.fixture
    def file_name(self):
        return 'test_subjects.csv'

    @pytest.fixture
    def log_file_name(self):
        return 'test_subjects.log'

    @pytest.fixture
    def subjects(self):
        return ['Математика', 'Информатика', 'Физика', 'Химия']

    @pytest.fixture
    def e_logger(self, log_file_name):
        return logging.getLogger(logging.basicConfig(
            filename=log_file_name, filemode='a+',
            format='%(asctime)s %(levelname)s %(message)s'))

    @pytest.fixture
    def student(self, file_name, e_logger, subjects):
        with open(file_name, mode='w', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(subjects)
        return Student('Петров', file_name, e_logger)

    def test_full_name(self, student):
        assert student.full_name == 'Петров'

    def test_add_grade_success(self, student):
        student.add_grade('Математика', 4)
        assert student.grades['Математика'][0] == [4]

    def test_add_grade_fail(self, student):
        student.add_grade('Биология', 4)
        assert 'Биология' not in student.grades

    def test_add_test_score_success(self, student):
        student.add_test_score('Математика', 99)
        assert student.grades['Математика'][1] == [99]

    def test_add_test_score_fail(self, student):
        student.add_test_score('Алгебра', 80)
        assert 'Алгебра' not in student.grades

    def test_get_average_grade(self, student):
        student.add_grade('Математика', 5)
        student.add_grade('Математика', 4)
        assert student.get_average_grade() == 4.5

    def test_get_average_test_score(self, student):
        student.add_test_score('Информатика', 100)
        student.add_test_score('Информатика', 50)
        assert student.get_average_test_score('Информатика') == 75
