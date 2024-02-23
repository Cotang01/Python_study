"""
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
"""


class Rectangle:
    """Class for creating Rectangle objects"""

    def __init__(self, *sides):
        match len(sides):
            case 1 | 2:
                self._width = sides[0]
                self._length = sides[-1]
                self._perimeter = (self.width + self.length) * 2
                self._area = self.width * self.length
            case _:
                raise ValueError(
                    f'{self.__class__.__name__} '
                    f'cannot have that amount of sides'
                )

    def _is_valid_size(self, value):
        if value < 0:
            raise ValueError('Side cannot have negative length')
        return True

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if self._is_valid_size(new_width):
            self._width = new_width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_length):
        if self._is_valid_size(new_length):
            self._width = new_length

    @property
    def perimeter(self):
        return self._perimeter

    @property
    def area(self):
        return self._area

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.length + other.length)

    def __sub__(self, other):
        if not self._is_valid_size(new_w := self.width - other.width) \
                or not self._is_valid_size(new_l := self.length - other.length):
            raise ValueError(f'New {self.__class__} cannot have negative size')
        return Rectangle(new_w, new_l)

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
