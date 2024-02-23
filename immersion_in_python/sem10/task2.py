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
        match len(sides):
            case 1 | 2:
                self.width = sides[0]
                self.length = sides[-1]
            case _:
                raise ValueError(
                    f'{self.__class__.__name__} '
                    f'cannot have that amount of sides'
                )

    def get_per(self):
        return (self.width + self.length) * 2

    def get_area(self):
        return self.width * self.length
