#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO generate collections in a more
# memory efficient way using generator functions.
"""
    Docstring:
"""

def get_numbers():
    """ Return a collection of numbers """
    numbers = []
    for x in range(0, 1000000000000):
        numbers.append(x)
    return numbers

def generate_numbers():
    """ Generator Function - Yield on value at a time from a collection """
    print("Executing generate_numbers..")
    for x in range(0, 10):
        yield x

# for z in get_numbers():
for z in generate_numbers():
    print(z)

# Alternatively we could use a while loop and the built-in next() function.
gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break

# Alternatively, requested the next yielded value manually..
gen = generate_numbers()
num1 = next(gen, False)
num2 = next(gen, False)
num3 = next(gen, False)
print(num1, num2, num3)