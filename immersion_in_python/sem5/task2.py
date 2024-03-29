"""
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""


def get_dict_from_str(s: str) -> dict[str: int]:
    return {k: ord(k) for k in s}
