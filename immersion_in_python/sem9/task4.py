"""
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""


def repeat(num: int):
    def decorator(func: callable):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator
