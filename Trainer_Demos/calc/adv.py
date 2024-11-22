#! /usr/bin/env python3
# Author: DCameron
# Description: This script is an advanced calculator app.
"""
    Advanced Calculator app with power, modulus and sqrt functions
"""
import sys

def power(x, z):
    """ Return the power of x to z as a float """
    return float(x**z)

def mod(x, z):
    """ Return the REMAINDER after the division of x and z as a float """
    return float(x%z)

def sqrt(x):
    """ Return the Square root of x as a float """
    return round(x**0.5, 3)

def main():
    print("##### Advanced Calc App #####")
    print(f"5 ** 2 = {power(5, 2)}")
    print(f"5 % 2 = {mod(5, 2)}")
    print(f"\N{square root}5 = {sqrt(5)}")
    return None

# Namespace Trick
if __name__ == "__main__":
    # EXECUTE only if ran directly as a program.
    # Ignore if imported.
    main()
    sys.exit(0)
