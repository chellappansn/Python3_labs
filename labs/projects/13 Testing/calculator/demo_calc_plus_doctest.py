"""
    Calculator program with add, divide, multiply, subtract and modulo functions.
"""

def add(*args):
    """ Return sum of x and z
    >>> add(4, 3)
    8
    >>> add(10, 20, 30)
    60
    """
    total = 0
    for num in args:
        total += num
    return total

def mul(*args):
    """ Return product of x and z
    >>> mul(4, 3)
    12
    """
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    """ Return x divided by z to 3 decimal places
    >>> div(4, 3)
    1.334
    """
    return float(f"{x/z:.3f}")

def main():
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 / 3 = {div(4, 3)}")
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()


