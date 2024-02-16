"""
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class FactorialsGenerator:
    """Class for generating number's factorial sequence
    based on provided start, stop, step values"""
    def __init__(self, stop: int, start: int = 1, step: int = 1):
        if not [*range(start, stop, step)]:
            raise ValueError('Cannot generate such sequence')
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        vals = [1]
        vals = [vals[-1] for i in range(1, self.stop)
                if not vals.append(i * vals[-1])][self.start::self.step]
        for num in vals:
            yield num
