
#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Advanced Collections - add, sub, mul, div

import sys
from adv import sqrt

def add(*args):
    """ Returns sum of all args as float """
    total = 0
    for num in args:
        total += num
    return float(total)

def sub(x, y):
    """ Returns sub of x and y as a float"""
    return float(x - y)

def mul(*args):
    """ Returns product of all args as float """
    total = 1
    for num in args:
        total *= num
    return total

def div(x,y):
    """ Returns divide of x and y as a float"""
    return round(x/y, 3)

def main():
    print ("*** Basic Calc App ***")
    print(f" 4 + 3 + 2 + 1 = { add(4, 3, 2, 1)}")
    print(f" 4 - 3 = { sub(4, 3)}")
    print(f" 4 * 3 * 2 * 1 = { mul(4, 3, 2, 1)}")
    print(f" 4 / 3 = { div(4, 3)}")

    print(f" Advance mode -> sqrt of 5 = {sqrt(5)}")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
