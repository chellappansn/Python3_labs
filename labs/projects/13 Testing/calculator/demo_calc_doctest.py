"""
    Calculator program with add, divide and multiply functions.
"""

def add(*args):
    """ Return sum of all parameters
    >>> add(4, 3)
    7

    """
    total = 0
    for num in args:
        total += num
    return total

def mul(*args):
    """ Return product of all parameters
    >>> mul(4, 3)
    12

    """
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    """ Return x divided by z o 3 decimal places
    >>> div(4, 3)
    1.333

    """
    return float(f"{x/z:.3f}")

def main():
    """ THe main program """
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 / 3 = {div(4, 3)}")
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

