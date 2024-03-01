"""
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
"""
import re
from immersion_in_python.logger import get_logger, logger_params
from datetime import datetime, date

logger = get_logger(*logger_params, 'task4.log')


def convert_to_date(s: str, logger) -> datetime:
    s = s.split(' ')
    weekday_count = int(''.join(filter(lambda x: x.isdigit(), s[0])))
    month = s[2].lower()
    weekdays = ('понедельник', 'вторник', 'среда', 'четверг',
                'пятница', 'суббота', 'воскресенье')
    valid_weekdays = '(?=(' + '|'.join(weekdays) + '))'
    month_start_pos = 1 + weekdays.index(
        re.findall(valid_weekdays, s[1].lower())[0])
    months = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
              'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
    month_pos = 1 + months.index([m for m in
                                  [m for m in months
                                   if m[:-2] == month[:-2]
                                   or len(month) - len(m) == 1]
                                  if m[0] == month[0]][0])
    first_day = date(day=1,
                     month=month_pos,
                     year=datetime.now().year).isoweekday()
    exact_day = ((1 + 7 * weekday_count - (first_day - month_start_pos))
                 if month_start_pos < first_day
                 else 1 + 7 * (weekday_count - 1) - (first_day - weekday_count))
    try:
        return datetime(datetime.now().year,
                        month_pos,
                        exact_day)
    except ValueError:
        logger.warning(f'{s} is incorrect format')
