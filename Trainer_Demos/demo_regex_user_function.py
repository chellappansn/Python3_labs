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
    try:
        fh_in = open(file, mode="rt")
    except PermissionError as err:
        print(f"Error {err.args[0]}, reason={err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as err:
        print(f"Error {err.args[0]}, reason={err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(2)
    except BaseException as err:
        print(f"Error occurred, investigate", file=sys.stderr)
        sys.exit(3)
    else:
        # Executes if try block is successful..
        lines = 0
        for line in fh_in:
            m = re.search(pattern, line)  # Search for pattern in each line of file.
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")

        fh_in.close() # Flush buffers and close file handle.
    finally:
        # Always executes if try block fails/succeeds
        print("And now for something completely different..")
    return lines

def main():
    search_pattern(r"^.{19}$", r"c:\labs\projects\Python3_labs\labs\wrds")
    # num_lines = search_pattern()
    # print(f"Matched {num_lines}")
    return None

# Namespace Trick
if __name__ == "__main__":
    main()
    sys.exit(0)