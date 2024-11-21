#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo a SAFER way of managing resources like
# file handles using a CONTEXT RESOURCE MANAGER (with statement).
"""
    Docstring:
"""
import sys
movies = { 'joe': ['lotr', 'rocky', 'interstellar'],
           'merrick': ['matrix', 'godfather', 'godfather II'],
           'niteen': ['godfather', '3idiots', 'benjamin button'],
           'brad': ['jaws', 'star wars', 'rocky'],
           'mahendran': ['top gun', 'terminator', 'rambo']
}

# Open file handle for WRITING in TEXT mode.
with open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name}: {movies[name]}", sep=" ", end="\n", file=sys.stdout)
        print(f"{name}: {movies[name]}", sep=" ", end="\n", file=fh_out)
        # fh_out.write(f"{name}: {movies[name]}\n")
    # End of Block, file handle is flushed and closes automatically.

print("-" * 60)

# Open file handle for READING in TEXT mode.
with open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")
