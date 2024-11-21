#! /usr/bin/env python3
# Author: DCameron
# Description: This script will clean and validate postcodes from the file
# postcodes.txt.
"""
    Docstring:
"""
import re
# Open file handle for READING in TEXT mode!
fh_in = open(r"c:\labs\projects\Python3_labs\labs\postcodes.txt", mode="rt")
valid = 0
invalid = 0

for postcode in fh_in:
    if postcode.isspace(): continue
    # QUES 1 solution
    postcode = postcode.upper()
    postcode = re.sub(r"\s+", r"", postcode)

    postcode = re.sub(r"(\d[A-Z]{2})$", r" \1", postcode) # Sub SPACE before last three chars!

    # Ques 2 solution
    m = re.search(r"^[A-Z]{1,2}\d{1,2}[A-Z]? \d[A-Z]{2}$", postcode)
    if m:
        valid += 1
        print(postcode)
    else:
        invalid += 1

fh_in.close()
print(f"Valid postcodes = {valid}") # Answer: 25
print(f"Invalid postcodes = {invalid}") # Answer: 5