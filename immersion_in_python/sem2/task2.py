data = [5, 'a', 2.0, [], {}, 5, 3.5]
for i, v in enumerate(data):
    print(i+1)
    print(v)
    print(id(v))
    print(v.__sizeof__())
    try:
        print(hash(v))
    except TypeError:
        pass
    print('Целое число') if isinstance(v, int) else None
    print('Строка') if isinstance(v, str) else None
    print('-'*15)
