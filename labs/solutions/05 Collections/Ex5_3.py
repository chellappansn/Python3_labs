#! /usr/bin/python
# Chapter 5 Exercise 3
"""
    Docstring: This program will generate 6 unique random lottery numbers.
"""

import random

lotto = set()           # Create an empty set.

while len(lotto) < 6:
    num = random.randint(1, 50)
    lotto.add(num)      # Add new number to set.


print("Lottery numbers = ", lotto)