#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define a VARIADIC function
# which is a function that allows a VARIABLE number of parameters!
"""
    This script provides functions for searching text files
    using regular expression patterns.
"""
import re

# Example of a user VARIADIC function that allows variable number of
# parameters.Unpack all remaining parameters in a TUPLE!
def search_pattern(pattern=r"^.{28}$", *files):
    """ Search for pattern in one or more files display lines
        return: num lines matched
    """
    for file in files:
        fh_in = open(file, mode="rt")
        lines = 0
        for line in fh_in:
            m = re.search(pattern, line)  # Search for pattern in each line of file.
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")

        fh_in.close() # Flush buffers and close file handle.
    return lines


search_pattern(r"^.{19}$", r"c:\labs\words", r"c:\labs\words2", r"c:\labs\words2")

