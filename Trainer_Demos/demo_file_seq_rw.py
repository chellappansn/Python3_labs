#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, close, and read, write and
# append sequentially to a TEXT file.
"""
    Docstring:
"""
movies = { 'joe': ['lotr', 'rocky', 'interstellar'],
           'merrick': ['matrix', 'godfather', 'godfather II'],
           'niteen': ['godfather', '3idiots', 'benjamin button'],
           'brad': ['jaws', 'star wars', 'rocky'],
           'mahendran': ['top gun', 'terminator', 'rambo']
}

# Open file handle for WRITING in TEXT mode.
fh_out = open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.txt", mode="wt")

# ITERATE through the dict keys and WRITE keys+values to filehandle.
for name in movies.keys():
    print(f"{name}: {movies[name]}")
    fh_out.write(f"{name}: {movies[name]}\n")

# fh_out.flush() # Manually flush buffers.
fh_out.close() # Flush buffers and close file handle.

print("-" * 60)
# Open file handle for READING in TEXT mode.
fh_in = open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str.Be Careful of Huge Files.
# text = fh_in.read(30) # Read NEXT 30 chars into str.
# text = fh_in.readline() # Read NEXT LINE into str.
# lines = fh_in.readlines() # Read ALL LINES into list object. Be Careful of HUGE files!
# print(f"First Line = {lines[0]}") # Good as you can index List to get specific lines.
# print(f"Last Line = {lines[-1]}")

# ITERATE through the file handle one line at a time
# using an ITERATOR for loop and file handle (Iterator Object = iter()/next())
# for line in open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.txt", mode="rt"):
for line in fh_in:
    print(line, end="")


fh_in.close() # Close file handle.
