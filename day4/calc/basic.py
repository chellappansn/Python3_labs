
#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Advanced Collections - add, sub, mul, div

def add(*args):
    total = 0
    for num in args:
        total += num
    return float(total)

def sub(x, y):
    return float(x - y)

def mul(*args):
    total = 1
    for num in args:
        total *= num
    return total

def div(x,y):
    return round(x/y, 3)

print ("*** Basic Calc App ***")
print(f" 4 + 3 + 2 + 1 = { add(4, 3, 2, 1)}")
print(f" 4 - 3 = { sub(4, 3)}")
print(f" 4 * 3 * 2 * 1 = { mul(4, 3, 2, 1)}")
print(f" 4 / 3 = { div(4, 3)}")