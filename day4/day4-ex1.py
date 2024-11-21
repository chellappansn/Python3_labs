
#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Advanced Collections

def frange (start, stop, step=0.25):
    begin = float(start)
    while begin < stop:
        yield begin
        begin += step

for num in frange (1,10):
    print(num)

for