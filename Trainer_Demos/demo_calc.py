#! /usr/bin/env python3
# Author: DCameron
# Description: This script is an ultra realistic calculator app.
"""
    Calculator App with add, multiply and divide functions.
"""

def add(x, z):
    """ Return SUM of the parameters """
    return float(x+z)

def mul(x, z):
    """ Return PRODUCT of the parameters """
    return float(x*z)

def div(x, z):
    """ Return Quotient of x divided by z to 3 decimal places """
    return round(x/z, 3)

print(f"4 + 3 = {add(4, 3)}")
print(f"4 * 3 = {mul(4, 3)}")
print(f"4 / 3 = {div(4, 3)}")

# Alternative method for defining a SIMPLE function without
# using the def statement. Usually used when you want to embed a
# function code inside another function call.
ladd = lambda x, z: float(x+z)
lmul = lambda x, z: float(x*z)
ldiv = lambda x, z: round(x/z, 3)

print(f"4 + 3 = {ladd(4, 3)}")
print(f"4 * 3 = {lmul(4, 3)}")
print(f"4 / 3 = {ldiv(4, 3)}")