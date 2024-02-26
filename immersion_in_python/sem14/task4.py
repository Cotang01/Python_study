"""
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import pytest
from immersion_in_python.sem14.task2 import keep_latin_and_spaces


@pytest.mark.parametrize('case, expected',
                         [('hello', 'hello'),
                          ('hello world', 'hello world'),
                          ('   ', '   ')])
def test_keep_latin_and_spaces_no_changes(case, expected):
    assert keep_latin_and_spaces(case) == expected


@pytest.mark.parametrize('case, expected',
                         [('HELLO', 'hello'),
                          ('HEllO', 'hello'),
                          ('HELLO wORlD', 'hello world')])
def test_keep_latin_and_spaces_change_case(case, expected):
    assert keep_latin_and_spaces(case) == expected


@pytest.mark.parametrize('case, expected',
                         [('hello, world', 'hello world'),
                          ('! . "" , ?', '    '),
                          ('www.example.com', 'wwwexamplecom')])
def test_keep_latin_and_spaces_rm_punctuation(case, expected):
    assert keep_latin_and_spaces(case) == expected


@pytest.mark.parametrize('case, expected',
                         [('привет user', ' user'),
                          ('приветствую', ''),
                          (' тест ', '  ')])
def test_keep_latin_and_spaces_rm_non_latin(case, expected):
    assert keep_latin_and_spaces(case) == expected


@pytest.mark.parametrize('case, expected',
                         [('Привет, User!', ' user'),
                          ('ñ: Spanish', ' spanish'),
                          ('   СiГaРeТa!   ', '   iaea   ')])
def test_keep_latin_and_spaces_change_case_rm_punct_rm_non_latin(case, expected):
    assert keep_latin_and_spaces(case) == expected
