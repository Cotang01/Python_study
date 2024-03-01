"""
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат
"""

from immersion_in_python.logger import get_logger, logger_params

logger = get_logger(*logger_params, 'task2.log')


def log_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.info(f'Func: {func}; Args: {args, kwargs}; Result: {res}')
        return res
    return wrapper
