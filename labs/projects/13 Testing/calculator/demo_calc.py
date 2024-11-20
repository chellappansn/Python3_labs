"""
    Calculator program with add, multiply, and divide functions.
"""

def add(*args):
    """ Returns the sum of all parameters. """
    total = 0
    for num in args:
        total += num
    return total

def mul(*args):
    """ Returns the product of all parameters. """
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    """ Returns x divided by z, as a float to 3 decimal places. """
    if z == 0:
        raise ZeroDivisionError("Divisor must be zero")
    return float(f"{x/z:.3f}")

def main():
    """ Manually Test the functions. """
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 / 3 = {div(4, 3)}")
    return None

if __name__ == "__main__":
    main()
