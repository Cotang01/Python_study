"""
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""
import json


def load_data_to_json(file_path: str):
    input_choices = 'Введите через пробел:\n' \
                    'Имя, id, уровень доступа\n' \
                    '-> '
    current_data = get_json_data(file_path)

    while True:
        n, p, l = get_input(input_choices, current_data)
        if n is None:
            break
        if l not in current_data:
            current_data[l] = {}
        current_data[l].update({p: n})
    write_json_data(file_path, current_data)


def get_input(input_choices, current_data: dict) -> \
        tuple[str, str, str] | tuple[None, None, None]:
    choice = input('Выберите действие:\n'
                   '1. Принять данные\n'
                   '2. Завершить программу\n'
                   '-> ')
    match choice:
        case '1':
            user_input = input(input_choices).lower().split()
            while not len(user_input) == 3 \
                    or not user_input[1].isdigit() \
                    or not user_input[2].isdigit() \
                    or not 0 < int(user_input[2]) < 8 \
                    or user_input[1] in current_data.keys():
                print('Данные введены неправильно или id существует')
                user_input = input(input_choices).lower().split()
            return (user_input[0].capitalize(),
                    user_input[1],
                    user_input[2])
        case '2':
            return None, None, None


def get_json_data(file_path: str) -> dict:
    try:
        with open(file_path, mode='r', encoding='UTF-8') as file:
            return json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        print("File is empty or data type doesn't match JSON")
        return {}


def write_json_data(file_path: str, data: dict) -> None:
    with open(file_path, mode='w', encoding='UTF-8') as file:
        file.write(json.dumps(data))
