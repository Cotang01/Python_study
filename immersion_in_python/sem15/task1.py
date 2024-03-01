"""
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
"""
from immersion_in_python.logger import get_logger, logger_params


logger = get_logger(*logger_params, 'task1.log')

try:
    res = 1/0
except ZeroDivisionError as zde:
    logger.warning(f'Divided by zero!: {zde.__traceback__.tb_frame}')
