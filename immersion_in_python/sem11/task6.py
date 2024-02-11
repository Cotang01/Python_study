"""
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""


class Rectangle:
    """Class for creating Rectangle objects"""

    def __init__(self, *sides):
        n = len(sides)
        if n == 1:
            self.side = sides[0]
            self.perimeter = self.side * 4
            self.area = self.side ** 2
        elif n == 2:
            self.width = sides[0]
            self.length = sides[1]
            self.perimeter = (self.width + self.length) * 2
            self.area = self.width * self.length
        else:
            raise ValueError(
                f"{self.__class__} cannot have {n} sides")

    def get_per(self):
        return self.perimeter

    def get_area(self):
        return self.area

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

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __le__(self, other):
        return self.area <= other.area

    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area >= other.area
