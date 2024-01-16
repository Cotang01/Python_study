"""
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировке Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

# with open(0) as inp == inp = input()

with open(0) as inp:
    data = sorted(inp.read()
                  .strip()
                  .replace('.', '')
                  .replace(',', '')
                  .split())
    biggest_len = 0
    for i in data:
        if len(i) > biggest_len:
            biggest_len = len(i)
    for i in range(len(data)):
        print(f'{i + 1} {data[i]:>{biggest_len}}')
