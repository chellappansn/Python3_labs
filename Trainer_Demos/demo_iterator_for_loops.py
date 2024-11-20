#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo howto ITERATE through a COLLECTION
# (str/tuples/list/dict/sets) using an ITERATOR for loop.
"""
    Docstring:
"""
import sys

#            0       1           2            4            5             6           7
films = ['snatch', 'lotr', '3.10 to yuma', 'top gun', 'godfather', 'fight club', 'casino']

# Iterate through a COLLECTION using an ITERATOR for loop.
for film in films:
    print(film.title(), end="\n")
print("Films = ", films)

# Iterate through a COLLECTION AND modify each value using
# an ITERATOR for loop and a counter.
idx = 0
for film in films:
    print(film.upper(), end="\n")
    films[idx] = film.upper()
    idx += 1
print("Films = ", films)

# Alternatively we could ITERATE through the collection and modify
# the values using an ITERATOR for loop plus enumerate() function.
for (idx, film) in enumerate(films, start=0):
    print(film.lower(), end="\n")
    films[idx] = film.lower()
print("Films = ", films)

print("Done.")

try:
    # sys.exit() can be caught using TRY block.
    sys.exit(0) # Explicitly EXIT script and return EXIT code (0=success, 1-255=error code)
except SystemExit:
    print("Exiting script..")
    sys.exit(15)
