"""
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""


class Cat:
    """Class for cats info"""
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.enemies = [Dog.__name__]

    def print_info(self):
        print(self.enemies)


class Dog:
    """Class for dogs info"""
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.enemies = [Cat.__name__]

    def print_info(self):
        print(self.enemies)


class Fox:
    """Class for fox info"""
    def __init__(self, name, colour, extraction):
        self.name = name
        self.colour = colour
        self.extraction: list[str] = extraction

    def print_info(self):
        print(self.extraction)
