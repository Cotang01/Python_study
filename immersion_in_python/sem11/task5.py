"""
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""


class Rectangle:
    """Class for creating Rectangle objects"""

    def __init__(self, *sides):
        match len(sides):
            case 1 | 2:
                self.width = sides[0]
                self.length = sides[-1]
                self.perimeter = (self.width + self.length) * 2
                self.area = self.width * self.length
            case _:
                raise ValueError(
                    f'{self.__class__.__name__} '
                    f'cannot have that amount of sides'
                )

    def _is_valid_size(self, value):
        if value < 0:
            raise ValueError('Side cannot have negative length')
        return True

    def __add__(self, other):
        new_per = self.perimeter + other.perimeter
        return Rectangle(new_per / 2 - self.width, new_per / 2 - other.length)

    def __sub__(self, other):
        new_per = self.perimeter - other.perimeter
        new_w = new_per / 2 - self.width
        new_l = new_per / 2 - other.length
        if not self._is_valid_size(new_w) or not self._is_valid_size(new_l):
            raise ValueError(f'New {self.__class__} cannot have negative size')
        return Rectangle(new_w, new_l)
