def write_tree(rows: int) -> None:
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))


write_tree(int(input('Введите высоту ёлки: -> ')))
