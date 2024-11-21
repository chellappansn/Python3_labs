#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, close, read and write
# RANDOMLY to a TEXT/BINARY file.
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

# Open file handle for READING in TEXT mode.
with open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, 0) # Seek forwards 90 chars from SOF.
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(130, 0)  # Seek forwards 90 chars from SOF.
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

print("-" * 60)

# Open file handle for READING in BINARY mode.
with open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.txt", mode="rb") as fh_data:
    fh_data.seek(-75, 2) # Seek back 75 bytes from EOF.
    text = fh_data.read(30)
    print(f"Text at {fh_data.tell() - len(text)} = {text}")

    fh_data.seek(-45, 1)  # Seek back 45 bytes from CURRENT byte pos.
    text = fh_data.read(30)
    print(f"Text at {fh_data.tell() - len(text)} = {text}")
