"""
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
"""


class Rectangle:
    """Class for creating Rectangle objects"""

    __slots__ = 'side', 'width', 'length', 'perimeter', 'area'

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
                f"{self.__class__.__name__} cannot have {n} sides")

    def _check_square_attr(self):
        if not hasattr(self, 'side'):
            raise AttributeError('Maybe you wanted to call width or length?')

    def _check_rect_attr(self):
        if not hasattr(self, 'width') or not hasattr(self, 'length'):
            raise AttributeError("Maybe you wanted to call square's side?")

    def _is_valid_size(self, value):
        if value < 0:
            raise ValueError('Side cannot have negative length')
        return True

    @property
    def side(self):
        self._check_square_attr()
        return self.side

    @side.setter
    def side(self, new_side):
        self._check_square_attr()
        if self._is_valid_size(new_side):
            self.side = new_side

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, new_width):
        self._check_rect_attr()
        if self._is_valid_size(new_width):
            self.width = new_width

    @property
    def length(self):
        return self.length

    @length.setter
    def length(self, new_length):
        self._check_rect_attr()
        if self._is_valid_size(new_length):
            self.width = new_length

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
