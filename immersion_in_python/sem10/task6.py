"""
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""
from abc import ABC


class Animal(ABC):
    """Base class for animals"""
    def __init__(self, name: str, colour: str):
        self.name = name
        self.colour = colour

    def print_info(self):
        for attr, val in vars(self).items():
            print(f"{attr}: {val}")


class Cat(Animal):
    """Class for cats info"""
    def __init__(self, name, colour):
        super().__init__(name, colour)
        self.enemies = [Dog.__name__]


class Dog(Animal):
    """Class for dogs info"""
    def __init__(self, name, colour):
        super().__init__(name, colour)
        self.enemies = [Cat.__name__]


class Fox(Animal):
    """Class for fox info"""
    def __init__(self, name, colour, extraction):
        super().__init__(name, colour)
        self.extraction: list[Animal] = extraction
