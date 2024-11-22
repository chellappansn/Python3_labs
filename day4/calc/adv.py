import sys


#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Advanced Calculator - power,modules, sqt

def power(x, y):
    """ Returns power of x and y as a float"""
    return float(x**y)

def mod(x,y):
    """ Returns mod of x and y as a float"""
    return float(x%y)

def sqrt(x):
    """ Returns square root of x as 3 digit double"""
    return round(x**0.5, 3)

def main():
    print ("--- Advance Calc App ---")
    print (f" 5 ** 2 = {power(5,2)}")
    print (f" 5 % 2 = {mod(5,2)}")
    print (f" 5 sqrt = {sqrt(5)}")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)