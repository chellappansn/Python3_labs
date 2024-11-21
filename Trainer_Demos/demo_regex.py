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

# ITERATE through the file handle one line at a time.
# using an ITERATOR for loop.
for line in fh_in:
    # Example of str testing.
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search(r"town", line) # Match lines with "town" in string.
    # m = re.search(r"^the", line)  # Match lines starting with "the".
    # m = re.search(r"ing$", line)  # Match lines ending with "ing".
    # m = re.search(r"^.ing$", line) # Match lines with char followed by "ing".
    # m = re.search(r"^[adr]ing$", line)  # Match lines with [adr] followed by "ing".
    # m = re.search(r"^[A-Z]", line)  # Match lines starting with a capital.
    # m = re.search(r"^...................$", line)  # Match lines with exactly 19 chars.
    # m = re.search(r"^.{19}$", line)  # Match lines with exactly 19 chars.
    # m = re.search(r"\.", line)  # Match lines with a DOT.
    # m = re.search(r"[aeiou][aeiou][aeiou]", line)  # Match lines with consecutive vowels".
    # m = re.search(r"[aeiou]{5,}", line)  # Match lines with at least 5 consecutive vowels".
    # m = re.search(r"^[A-Z].*[A-Z]$", line)  # Match lines start/end with a CAPITAL.
    # m = re.search(r"^[A-Z].{3}[A-Z]$", line)  # Match lines of 5 chars start/end with a CAPITAL.
    # m = re.match(r"[A-Z].{3}[A-Z]$", line)  # Match LINES STARTING with AUTOMATICALLY!
    # m = re.fullmatch(r"^[A-Z].{3}[A-Z]$\n", line)  # MUST Match ENTIRE line including HIDDEN chars!
    m = re.search(r"^(.)(.).\2\1$", line)  # Match 5 char palindromes! Remember RAW string!
    # m = re.search(r"^([A-Z]).*\1$", line)  # Match lines start/end with SAME CAPITAL!
    # m = re.search(r"^([A-Z]).*\1$", line, flags=re.IGNORECASE)  # AND IGNORE case in search!
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}, "
              f"Groupings = {m.groups()}, Group 1 = {m.group(1)}")

fh_in.close() # Flush buffers and close file handle.