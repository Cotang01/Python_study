"""
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import unittest
from immersion_in_python.sem14.task2 import keep_latin_and_spaces


class TestKeepLatinAndSpaces(unittest.TestCase):

    def test_keep_latin_and_spaces_no_changes(self):
        test_params = [('hello', 'hello'),
                       ('hello world', 'hello world'),
                       ('   ', '   ')]
        for case, expected in test_params:
            with self.subTest(msg='Testing if func doesnt change str',
                              case=case,
                              expected=expected):
                self.assertEqual(keep_latin_and_spaces(case), expected)

    def test_keep_latin_and_spaces_change_case(self):
        test_params = [('HELLO', 'hello'),
                       ('HEllO', 'hello'),
                       ('HELLO wORlD', 'hello world')]
        for case, expected in test_params:
            with self.subTest(msg='Testing if func changing case to lower',
                              case=case,
                              expected=expected):
                self.assertEqual(keep_latin_and_spaces(case), expected)

    def test_keep_latin_and_spaces_rm_punctuation(self):
        test_params = [('hello, world', 'hello world'),
                       ('! . "" , ?', '    '),
                       ('www.example.com', 'wwwexamplecom')]
        for case, expected in test_params:
            with self.subTest(msg='Testing if func removes punctuation',
                              case=case,
                              expected=expected):
                self.assertEqual(keep_latin_and_spaces(case), expected)

    def test_keep_latin_and_spaces_rm_non_latin(self):
        test_params = [('привет user', ' user'),
                       ('приветствую', ''),
                       (' тест ', '  ')]
        for case, expected in test_params:
            with self.subTest(msg='Testing if func removes non latin letters',
                              case=case,
                              expected=expected):
                self.assertEqual(keep_latin_and_spaces(case), expected)

    def test_keep_latin_and_spaces_change_case_rm_punct_rm_non_latin(self):
        test_params = [('Привет, User!', ' user'),
                       ('ñ: Spanish', ' spanish'),
                       ('   СiГaРeТa!   ', '   iaea   ')]
        for case, expected in test_params:
            with self.subTest(msg='Testing if func changes case to '
                                  'lower, removes punctuation and removes non '
                                  'latin letters all together',
                              case=case,
                              expected=expected):
                self.assertEqual(keep_latin_and_spaces(case), expected)


if __name__ == '__main__':
    unittest.main()
