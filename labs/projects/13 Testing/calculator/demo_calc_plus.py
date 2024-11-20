"""
    Calculator program with add, subtract, multiply, divide and modulo functions.
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
    return float(f"{x/z:.3f}")

def sub(x, z):
    """ Returns the result of x minus z. """
    return x - z

def mod(x, z):
    """ Returns the remainder of x modulus y. """
    return x % z

def main():
    """ Manually Test the functions. """
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 / 3 = {div(4, 3)}")
    print(f"4 - 3 = {sub(4, 3)}")
    print(f"4 % 3 = {mod(4, 3)}")
    return None

if __name__ == "__main__":
    main()
