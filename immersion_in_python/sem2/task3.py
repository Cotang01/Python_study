def transform_to_num_system(num: int, system: int) -> str:
    """
    A function that transforms number num into different numeric system.
    """
    res = []
    while num > 0:
        whole_part = num // system
        to_remove = whole_part * system
        res.append(str(num - to_remove))
        num = whole_part
    return ''.join(res[::-1])


assert transform_to_num_system(255, 2) == bin(255)[2:]
assert transform_to_num_system(1212, 8) == oct(1212)[2:]
