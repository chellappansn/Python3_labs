#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO copy and optionally filter collections
# to a destination collections using different methods..
"""
    Docstring:
"""

pets = ['romeo', 'sadie', 'petey', 'max', 'baily', 'maggie', 'pennie', 'toto', 'bentley', 'toto']

# Copy and filter the source collection..
# 1.Using an iterator loop + collection, if condition (filtering), and expression.
wee_names = []
for pet_name in pets: # 1.Iterator loop plus source collection.
    if len(pet_name) <= 5: # 2.Optional condition (filtering).
        wee_names.append(pet_name.title()) # 3.Expression.
print(f"1.Short names = {wee_names}")

def filter_names(name):
    """ Return True if parameter is less than 6 chars in length """
    if len(name) <= 5:
        return True
    else:
        return False

# 2.Using an iterator loop + collection, user function (filtering), and expression.
wee_names = []
for pet_name in pets: # 1.Iterator loop plus source collection.
    if filter_names(pet_name): # 2.Optional condition (filtering).
        wee_names.append(pet_name.title()) # 3.Expression.
print(f"2.Short names = {wee_names}")

# 3.Using the built-in filter function + collection, user function (filtering)
wee_names = list(filter(filter_names, pets))
print(f"3.Short names = {wee_names}")

# 4.Using the built-in filter function + collection, lambda function (filtering)
wee_names = list(filter(lambda name:len(name) <= 5, pets))
print(f"4.Short names = {wee_names}")

# 5.LIST Comprehension - expression, for loop + collection, option if (filtering)
wee_names = [ pet_name.title() for pet_name in pets if len(pet_name) <= 5 ]
print(f"5.Short names = {wee_names}")

# 5.1 LIST Comprehension - expression, for loop + collection, option if (filtering)
wee_names = [ (pet_name.title(), len(pet_name)) for pet_name in pets if len(pet_name) <= 5 ]
print(f"5.1 Short names = {wee_names}")

# 5.2 DICT Comprehension - expression, for loop + collection, option if (filtering)
# EXTRA FILTERING - remove duplicate keys!
wee_names = { pet_name.title(): len(pet_name) for pet_name in pets if len(pet_name) <= 5 }
print(f"5.2 Short names = {wee_names}")

# 5.3 SET Comprehension - expression, for loop + collection, option if (filtering)
# EXTRA FILTERING - remove duplicate VALUES!
wee_names = { pet_name.title() for pet_name in pets if len(pet_name) <= 5 }
print(f"5.3 Short names = {wee_names}")