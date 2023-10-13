def add_integer(a, b=98):
    """
    Adds two integers or floats together and returns the result as an integer.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
