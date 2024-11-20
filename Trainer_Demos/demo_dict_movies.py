#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create, grow, shrink and access keys
# and values in a dictionary (UNORDERED Collection with UNIQUE KEYS).
# From Py3.6, dict keys are in INSERTION ORDER.
"""
    Docstring:
"""
import pprint

# Example of a multi-dimensional dict of lists!
movies = { 'joe': ['lotr', 'rocky', 'interstellar'],
           'merrick': ['matrix', 'godfather', 'godfather II'],
           'niteen': ['godfather', '3idiots', 'benjamin button']
}

# Add to a dict.
movies['brad'] = ['jaws', 'star wars', 'rocky']
movies['mahendran'] = ['top gun', 'terminator', 'rambo']

print(f"Joe's favourite movies are {movies['joe']}")
print(f"Joe's favourite movies are {movies.get('joe')}")
print(f"Joe's ultimate movie is {movies['joe'][0]}")

# films = movies.copy() # Copy Dictionary.
# films.clear() # Empty dictionary.

# Shrink a dict.
movies.pop('niteen') # Pop/remove key+value
movies.popitem() # Removes LAST INSERTED key+value
print("-" * 60)
pprint.pprint(movies)
print("-" * 60)

# ITERATE through the dict keys using an ITERATOR for loop and
# .keys() method.
for name in movies.keys():
    print(f"{name} likes {movies[name]}")

print("-" * 60)
# ITERATE through the dict VALUES using an ITERATOR for loop and
# .values() method.
for films in movies.values():
    print(films)

print("-" * 60)
# ITERATE through the dict keys+VALUES using an ITERATOR for loop and
# .items() method.
for (name, films) in movies.items():
    print(f"{name} loves {films}")