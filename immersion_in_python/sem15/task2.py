"""
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
"""
from immersion_in_python.logger import get_logger, logger_params

logger = get_logger(*logger_params, 'task2.log')


def log_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.info(f'Args: {args, kwargs}; Result: {res}')
        return res
    return wrapper
