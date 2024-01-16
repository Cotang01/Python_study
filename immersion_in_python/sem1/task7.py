def get_magic(num: int) -> int:
    match len(str(num)):
        case 1:
            return num**2
        case 2:
            list_num = [_ for _ in str(num)]
            return int(list_num[0]) * int(list_num[-1])
        case 3:
            return int(str(num)[::-1])
        case _:
            get_magic(int(input('Введите число: ->')))
