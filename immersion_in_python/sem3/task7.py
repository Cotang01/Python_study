"""
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
"""
from collections import Counter

# inp = input('-> ')
inp = '98yf297ynf72m9huhfm87hvmiuohVIP3UHRVP9238H387Y2387VG870M HGUYH4T3OHuyg'

res = {c: inp.count(c) for c in inp}
print(res)

res2 = {k: v for k, v in Counter(inp).items()}
print(res2)

res3 = {c: len([i for i in inp if i == c]) for c in inp}
print(res3)
