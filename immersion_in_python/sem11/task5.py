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

    def __add__(self, other):
        if hasattr(self, 'side') and hasattr(other, 'side'):
            return Rectangle(self.side + other.side)
        if not hasattr(self, 'side') and hasattr(other, 'side'):
            return Rectangle(self.width + other.side,
                             self.length + other.side)
        if hasattr(self, 'side') and not hasattr(other, 'side'):
            return Rectangle(self.side + other.width,
                             self.side + other.length)
        if not hasattr(self, 'side') and not hasattr(other, 'side'):
            return Rectangle(self.width + other.width,
                             self.length + other.length)

    def __sub__(self, other):
        if hasattr(self, 'side') and hasattr(other, 'side'):
            new_side = self.side - other.side
            if new_side < 0:
                raise ValueError(f'New side {new_side} should be positive')
            return Rectangle(self.side - other.side)
        if not hasattr(self, 'side') and hasattr(other, 'side'):
            new_width = self.width - other.side
            if new_width < 0:
                raise ValueError(f'New width {new_width} should be positive')
            new_length = self.length - other.side
            if new_length < 0:
                raise ValueError(f'New length {new_length} should be positive')
            return Rectangle(new_width, new_length)
        if hasattr(self, 'side') and not hasattr(other, 'side'):
            new_width = self.side - other.width
            if new_width < 0:
                raise ValueError(f'New width {new_width} should be positive')
            new_length = self.side - other.length
            if new_length < 0:
                raise ValueError(f'New length {new_length} should be positive')
            return Rectangle(new_width, new_length)
        if not hasattr(self, 'side') and not hasattr(other, 'side'):
            new_width = self.width - other.width
            if new_width < 0:
                raise ValueError(f'New width {new_width} should be positive')
            new_length = self.length - other.length
            if new_length < 0:
                raise ValueError(f'New length {new_length} should be positive')
            return Rectangle(new_width, new_length)
