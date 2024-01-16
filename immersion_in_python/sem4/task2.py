"""
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def sort_char_unicode(s: str) -> list[int]:
    return sorted([ord(c) for c in set(s)], reverse=True)
