def add_int(a: int, b: int):
    if any(not isinstance(arg, int) for arg in [a, b]):
        raise TypeError("Received non-integer arguments.")
    return a + b
