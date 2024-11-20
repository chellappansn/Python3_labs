def add(*args):
    total = 0
    for num in args:
        total += num
    return total

def sub(x, z):
    return x - z

def mul(*args):
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    return float(f"{x/z:.3f}")

def mod(x, z):
    return x % z

def main():
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 / 3 = {div(4, 3)}")
    return None

if __name__ == "__main__":
    main()

