"""
2. Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК. Соберите информацию о содержимом в виде объектов
namedtuple. Каждый объект хранит: имя файла без расширения или название
каталога, расширение, если это файл, флаг каталога, название родительского
каталога. Написать 3-5 тестов к задаче.
"""
import argparse
import os
from collections import namedtuple
from typing import List
import pytest
import shutil


def gen_file_data(dir_path: str) -> List[namedtuple]:
    FileData = namedtuple('FileData',
                          ['name', 'ext', 'is_dir', 'parent_dir'])
    return [FileData(
        name=file.split('.')[0]
        if not os.path.isdir(os.path.join(dir_path, file)) else file,
        ext=file.split('.')[-1]
        if not os.path.isdir(os.path.join(dir_path, file)) else '',
        is_dir=os.path.isdir(os.path.join(dir_path, file)),
        parent_dir=os.path
        .abspath(dir_path)
        .split(os.path.sep)[-1])
        for file in os.listdir(dir_path)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command line args parser')
    parser.add_argument('dir_path', default='.', type=str,
                        help="path to dir to collect data from")
    line_args = parser.parse_args()
    res = gen_file_data(line_args.dir_path)
    print(res)


@pytest.fixture
def temp_dir():
    """
    Fixture that creates temporary dir 'test_dir' with 4 elements inside:
    2 empty dirs 'a' and 'b'
    2 files 'c.py' and 'd.txt'
    and returns temp dir name

    Clears temp dir afterwards
    """
    os.mkdir('test_dir')
    d_name = 'test_dir'
    os.makedirs(os.path.join(d_name, 'a'))
    os.makedirs(os.path.join(d_name, 'b'))
    with open(os.path.join(d_name, 'c.py'), 'w', encoding='UTF-8') as f1:
        f1.write('# test1')
    with open(os.path.join(d_name, 'd.txt'), 'w', encoding='UTF-8') as f1:
        f1.write('test2')
    yield d_name
    shutil.rmtree(d_name)


@pytest.fixture
def file_data():
    return namedtuple('FileData',
                      ['name', 'ext', 'is_dir', 'parent_dir'])


def test_gen_file_data_correct_file_name(temp_dir, file_data):
    res = gen_file_data(temp_dir)
    expected = file_data(
        name='a', ext='', is_dir=True, parent_dir='test_dir')
    assert res[0].name == expected.name


def test_gen_file_data_correct_file_ext(temp_dir, file_data):
    res = gen_file_data(temp_dir)
    expected = file_data(
        name='c', ext='txt', is_dir=False, parent_dir='test_dir')
    assert res[3].ext == expected.ext


def test_gen_file_data_is_dir(temp_dir, file_data):
    res = gen_file_data(temp_dir)
    expected = file_data(
        name='a', ext='', is_dir=True, parent_dir='test_dir')
    assert res[0].is_dir == expected.is_dir


def test_gen_file_data_correct_parent_dir(temp_dir, file_data):
    res = gen_file_data(temp_dir)
    expected = file_data(
        name='b', ext='', is_dir=True, parent_dir='test_dir')
    assert res[1].parent_dir == expected.parent_dir


def test_gen_file_data_correct_size(temp_dir, file_data):
    assert len(gen_file_data(temp_dir)) == 4