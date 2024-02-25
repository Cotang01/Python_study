"""
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Side:
    """Rectangle's side descriptor"""
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f'Size of {instance} cannot be negative: {value}')
        setattr(instance, self.name, value)


class Rectangle:
    """Class for creating Rectangle objects"""

    _width = Side()
    _length = Side()
    _attrs = {'width', 'length'}

    def __new__(cls, *sides):
        if any(filter(lambda x: x < 0, sides)):
            raise ValueError(f'Size of {cls} side cannot be negative')
        return super().__new__(cls)

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

    def __str__(self):
        return f"{[(k, v) for k, v in vars(self).items()]}"

    def __setattr__(self, key, value):
        if key != f'_{self.__class__.__name__}_attrs':
            if key in self._attrs:
                super().__setattr__(key, value)

    @property
    def perimeter(self):
        return (self.width + self.length) * 2

    @property
    def area(self):
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.length + other.length)

    def __sub__(self, other):
        return Rectangle(self.width - other.width, self.length - other.length)

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
