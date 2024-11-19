#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Leap year

"""
   Docstring
"""

num = input("Enter the year: ")

if int(num) %4 == 0 :
    print("Leap year is", num)
else:
    print ("Not an leap year", num)