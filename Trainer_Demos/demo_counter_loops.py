#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo how to REPEAT a block
# of commands a specific num of times using a COUNTER LOOP.
"""
    Docstring:
"""

count = 0 # 1.Initialise counter.
while count < 10: # 2.Loop condition.
    print(count)
    count += 1 # 3.Increment counter.

# Python has an alternative way of repeating commands using a
# for loop plus built-in range(start, stop, step) function.
for num in range(0, 10, 1):
    print(num)

# range(start, stop, step=1)
for num in range(0, 10):
    print(num)

# range(start=0, stop, step=1)
for num in range(101):
    print(num)
