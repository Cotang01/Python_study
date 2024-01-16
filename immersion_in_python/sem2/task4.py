def get_area_and_per(diam: int | float = 0) -> tuple[float, float]:
    """
    A function that returns area and length of circle based on provided
    diameter. By default, returns 0.
    """
    rad = round(diam / 2, 42)
    return round(rad ** 2 * 3.14, 42), round(2 * rad * 3.14, 42)
