
#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Advanced Calculator - power,modules, sqt


def power(x, y):
    return float(x**y)

def mod(x,y):
    return float(x%y)

def sqrt(x):
    return round(x**0.5, 3)

print ("--- Advance Calc App ---")
print (f" 5 ** 2 = {power(5,2)}")
print (f" 5 % 2 = {mod(5,2)}")
print (f" 5 sqrt = {sqrt(5)}")
