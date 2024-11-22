#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO match text data from a file
# using str and pattern matching and the re module.
"""
    Docstring:
"""
import re
import sys

# Example of a user function with parameter passing and default values.
def search_pattern(pattern=r"^.{28}$", file=r"c:\labs\projects\Python3_labs\labs\words"):
    fh_in = open(file, mode="rt")
    lines = 0
    reobj = re.compile(pattern) # Precompiling Pattern ONCE only!
    for line in fh_in:
        # m = re.search(pattern, line)  # Search for pattern in each line of file.
        m = reobj.search(line)
        if m:
            lines += 1
            print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")

    fh_in.close() # Flush buffers and close file handle.
    return lines

def main():
    search_pattern(r"^.{19}$", r"c:\labs\projects\Python3_labs\labs\words")
    # num_lines = search_pattern()
    # print(f"Matched {num_lines}")
    return None

if __name__ == "__main__":
    import cProfile
    # cProfile.run("main()") # Analyse/benchmark code to the console.
    cProfile.run("main()", "stats.prof")  # Analyse/benchmark to a file
    # main()
    sys.exit(0)