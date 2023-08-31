import random


def create_from_int(degree: int) -> dict:  # Создание многочлена через int
    poly = {}  # Создаём пустой словарь, где ключами будут степени
    # многочлена, а их значениями - коэффициенты
    for i in range(degree, -1, -1):  # Ключи будут идти от degree до -1 (
        # чтобы включительно был 0) с шагом в -1 (чтобы степени шли от
        # большего к меньшему
        coef = random.randint(-100, 100)  # Коэффициенты от -100 до 100
        if coef:
            poly[i] = coef  # После каждой генерации ключа присваиваем ему
            # значение переменной coef
    return poly  # В конце возвращаем словарь


def create_from_str(poly: str) -> dict:  # Создание многочлена через str
    # (В КОДЕ НЕ ПРИМЕНЯЕТСЯ)
    new_poly = {}  # Создаём пустой словарь
    poly = poly.replace(' ', '').replace('+', ' ').replace('-', ' -')  #
    # Убираем из строки пробелы и плюсы, а минусу добавляем спереди пробел,
    # чтобы сохранить отрицательный коэффициент
    if poly.endswith('=0'):  # Убираем =0 из строки, чтобы не мешался
        poly = poly[:-2]
    poly = poly.split()  # Делаем список из строки, разделяя все элементы
    for item in poly:  # Проходимся по списку
        if not item.startswith('0'):
            if '*x**' in item:
                new_element = item.split('*x**')
                new_poly[int(new_element[1])] = int(new_element[0])
            elif '*x' in item:
                new_poly[1] = int(item.replace('*x', ''))
            else:
                new_poly[0] = int(item)
    return new_poly


def str_from_dict(poly: dict) -> str:  # Делаем из словаря многочлен
    new_poly = []  # Создаём список, куда будут закидываться элементы
    for degree, coef in poly.items():  # Проходимся по ключам и значениям
        if coef > 0:  # Если коэффициент больше 0
            new_poly.append(f'{coef}*x**{degree}' if coef != 1 else
                            f'x**{degree}')
        else:  # Если коэффициент меньше 0
            new_poly.append(f'{coef}*x**{degree}' if coef != 1 else
                            f'-x**{degree}')
    return ' + '.join(new_poly).replace('+ -', '- '). \
        replace('**1 ', ' ').replace('*x**0', '') + ' = 0'  # Между всеми
    # добавляем +, а если уже есть -, то меняем '+ -' на '-', убираем из
    # строки элементы со степенью 1, последнему элементу не нужно *x**0 и в
    # конце добавляем '= 0'


def add_poly(first: dict, second: dict) -> dict:  # Соединяем наши два словаря
    final_dict = {}  # Создаём пустой словарь
    all_keys = list(set(list(first.keys()) + list(second.keys())))  # Делаем
    # список, где элементами будут суммы ключей первого и второго словаря
    # соответственно
    all_keys.sort(reverse=True)
    for key in all_keys:
        final_dict[key] = first.get(key, 0) + second.get(key, 0)
    return final_dict


first_poly = create_from_int(7)  # Создаём первый словарь с высшей степенью 7
second_poly = create_from_int(9)  # Создаём второй словарь с высшей степенью 9
third_poly = add_poly(first_poly, second_poly)  # Финальный словарь

# print(first_poly)
# print(second_poly)
print(third_poly)

first_poly = str_from_dict(first_poly)  # Делаем строку из первого словаря
second_poly = str_from_dict(second_poly)  # Делаем строку из второго словаря
third_poly = str_from_dict(third_poly)  # Делаем строку из финального словаря

# print(first_poly)
# print(second_poly)
print(third_poly)
