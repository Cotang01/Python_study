"""
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""

data = {
    '1friend': (2, 4, 3),
    '2friend': (4, 5, 6),
    '3friend': (3, 4, 5)
}

# Предметы, которые есть у всех
common_items = set.intersection(*[set(items) for items in data.values()])

# Всего какие есть предметы
all_items = set.union(*[set(items) for items in data.values()])

unique_items = set()
# Проверка каждого предмета на наличие в каждом мешке
for i in all_items:
    counter = 0
    for bag in data.values():
        if i in bag:
            counter += 1
    if counter == 1:
        unique_items.add(i)

missing_items = set()
for i in all_items:
    times_seen = 0
    for bag in data.values():
        if i in bag:
            times_seen += 1
    if len(data.values()) - times_seen == 1:
        missing_items.add(i)

missing_items_with_friends = set()
for item in missing_items:
    for k, v in data.items():
        if item not in v:
            missing_items_with_friends.add((k, item))

print(f'Взяли все: {common_items}')
print(f'Уникальные вещи: {unique_items}')
print(f'Вещи, которые есть у всех кроме одного: {missing_items_with_friends}')
