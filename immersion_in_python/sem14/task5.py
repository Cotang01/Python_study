"""
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""
from immersion_in_python.sem12.task6 import Rectangle
import unittest


class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.rect1_add_test = Rectangle(4)  # (4, 4)
        self.rect2_add_test = Rectangle(8)  # (8, 8)
        self.rect1_sub_test = Rectangle(4, 8)
        self.rect2_sub_test = Rectangle(6, 12)

    def test_add_rectangles(self):
        result = self.rect1_add_test + self.rect2_add_test
        expected = Rectangle(12, 12)
        self.assertEqual(result, expected)

    def test_sub_rectangles_correct(self):
        result = self.rect2_sub_test - self.rect1_sub_test
        expected = Rectangle(2, 4)
        self.assertEqual(result, expected)

    def test_sub_rectangles_raises_ve(self):
        with self.assertRaises(ValueError):
            self.rect1_sub_test - self.rect2_sub_test
