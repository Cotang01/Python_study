def is_leap_year(year: int):
    if year == 1582:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


print(is_leap_year(int(input('Год: -> '))))
