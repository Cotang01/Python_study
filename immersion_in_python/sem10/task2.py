"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    """Class for creating Rectangle objects"""
    def __init__(self, *sides):
        n = len(sides)
        if n == 1:
            self.side = sides[0]
        elif n == 2:
            self.width = sides[0]
            self.length = sides[0]
        else:
            raise ValueError(
                f"{self.__class__} cannot have {n} sides")

    def get_per(self):
        if hasattr(self, 'side'):
            return self.side*4
        return (self.width + self.length) * 2

    def get_area(self):
        if hasattr(self, 'side'):
            return self.side**2
        return self.width * self.length
