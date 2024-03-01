"""
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
"""
import argparse
import logging
import re
from datetime import datetime, date


def convert_to_date(s: str, logger) -> datetime:
    s = s.split(' ')
    weekday_count = int(''.join(filter(lambda x: x.isdigit(), s[0])))
    month = s[2].lower() if not s[2].isdigit() else int(s[2])
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
                                  if m[0] == month[0]][0]) \
        if not isinstance(month, int) else month
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


if __name__ == '__main__':
    lgr = logging.getLogger(logging.basicConfig(
        filename='task5.log', filemode='a+',
        format='%(asctime)s %(levelname)s %(message)s'))

    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('--month_start_day', type=str, default='1-й')
    parser.add_argument('--cur_weekday', type=str, default='Понедельник')
    parser.add_argument('--month', type=str, default='Январь')
    args = parser.parse_args()

    res = convert_to_date(' '.join([args.month_start_day, args.cur_weekday,
                                    args.month]), logger=lgr)
    print(res)
