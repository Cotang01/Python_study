def count_with_exceptions(n: int, e: int) -> int:
    """ Посчитайте сумму чётных элементов от 1 до n исключая кратные e. """
    res = 0
    to_except = {_ for _ in range(0, n, e)}  # создаём множество исключаемых
    for i in range(1, n):
        if i not in to_except:
            res += i
    return res
