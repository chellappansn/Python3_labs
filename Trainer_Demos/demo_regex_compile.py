#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO match text data from a file
# using str and pattern matching and the re module.
"""
    Docstring:
"""
import re

# Open file handle for READING in TEXT mode.
fh_in = open(r"c:\labs\projects\Python3_labs\labs\words", mode="rt")

reobj = re.compile(r"^.{19}$") # Pre-compile PATTERN ONLY ONCE!

for line in fh_in:
    # m = re.search(r"^.{19}$", line)  # Match lines of 19 chars
    m = reobj.search(line) # Use PRECOMPILED PATTERN for performance!
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")

fh_in.close() # Flush buffers and close file handle.
