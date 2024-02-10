"""
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
from math import pi
from dataclasses import dataclass


@dataclass
class Circle:
    """Class for creating Circle objects"""
    radius: int | float

    def get_per(self):
        """Method returning perimeter value of self Circle obj"""
        return 2 * pi * self.radius

    def get_area(self):
        """Method returning area value of self Circle obj"""
        return pi * self.radius ** 2
