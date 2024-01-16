"""
Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

data = (2, 3, 4, 'a', 'data', [], {}, 2.0, 2.5, 13)
res = {}
for i in data:
    if type(i) not in res:
        res[type(i)] = [v for v in data if isinstance(v, type(i))]

print(res)

res2 = {}
for i in data:
    res2[type(i)] = res2.get(type(i), [])
    res2.get(type(i)).append(i)

print(res2)
