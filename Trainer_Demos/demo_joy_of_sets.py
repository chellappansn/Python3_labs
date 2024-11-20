#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create, grow and shrink, and combine SETS
# using SET operators (Remember VENN diagrams from school).
# SETS are Collections with no keys and unique objects (no duplicates)
"""
    Docstring:
"""

marvel_fans = {'donald', 'javier', 'thomas', 'brad', 'merrick', 'joe'}
dc_fans = set() # Create an empty SET

# Grow a set.
dc_fans.add('donald')
dc_fans.add('niteen')
dc_fans.add('earl')

# Shrink a set
# dc_fans.pop() # Randomly remove a value!
# dc_fans.clear() # Empty the set!

print(f"Marvel fans = {marvel_fans}")
print(f"DC fans = {dc_fans}")

print("-" * 60)
# Combine SETS using SET operations (Remember VENN diagrams)
print(f"Fans of Either Marvel or DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of BOTH Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of ONLY Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 60)
# Combine SETS using SET OPERATORS (Remember VENN diagrams)
print(f"Fans of Either Marvel or DC = {marvel_fans | dc_fans}")
print(f"Fans of BOTH Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")
print(f"Fans of ONLY Marvel OR DC = {marvel_fans ^ dc_fans}")