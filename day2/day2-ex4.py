#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Range of numbers by step of -2

"""
   Collections
"""
import sys

var = input ("Please enter a integer:")

if var.isdecimal():
    print("you entered value is integer")
else:
    print("you entered value is NOT integer")
    sys.exit(0)

for num in range(int(var), -1, -2):
    print(num)
