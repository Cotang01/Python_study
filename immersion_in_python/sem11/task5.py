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
        n = len(sides)
        if n == 1:
            self.side = sides[0]
        elif n == 2:
            self.width = sides[0]
            self.length = sides[1]
        else:
            raise ValueError(
                f"{self.__class__} cannot have {n} sides")

    def get_per(self):
        if hasattr(self, 'side'):
            return self.side * 4
        return (self.width + self.length) * 2

    def get_area(self):
        if hasattr(self, 'side'):
            return self.side ** 2
        return self.width * self.length

    def increase(self, *sides):
        n = len(sides)
        if n == 1:
            new_side = self.side + sides[0]
            return Rectangle(new_side)
        elif n == 2:
            new_width = self.width + sides[0]
            new_length = self.length + sides[1]
            return Rectangle(new_width, new_length)
        else:
            raise ValueError(
                f"{self.__class__} cannot have {n} sides")

    def decrease(self, *sides):
        n = len(sides)
        if n == 1:
            new_side = self.side - sides[0]
            if new_side < 0:
                raise ValueError('Sides cannot have negative len')
            return Rectangle(new_side)
        elif n == 2:
            new_width = self.width - sides[0]
            new_length = self.length - sides[1]
            if new_width < 0 or new_length < 0:
                raise ValueError('Sides cannot have negative len')
            return Rectangle(new_width, new_length)
        else:
            raise ValueError(
                f"{self.__class__} cannot have {n} sides")
