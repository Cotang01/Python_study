"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json


def convert_to_json(file_path: str) -> None:
    with open(file_path, mode='r', encoding='UTF-8') as file1:
        data = [d.strip().split('|') for d in file1.readlines()]
    with open('task1.json', mode='w', encoding='UTF-8') as file2:
        file2.write(json.dumps(str({p[0]: p[-1] for p in data})))
