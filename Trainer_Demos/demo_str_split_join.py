#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo howto SPLIT and rejoin Strings
# using the str .split() and .join() methods.
"""
    Docstring:
"""

# Sample line from /etc/passwd on linux for the root user account.
# AND I want to modify the string! BUT str are IMMUTABLE!
#        0   1 2 3        4          5      6
line = "root:x:0:0:The Super User:/root:/bin/ksh"

fields = line.split(":") # Return a MUTABLE list of objects.
fields[4] = "The Administrator"
fields[6] = "/bin/bash"

line = ":".join(fields) # Return a NEW string separated with a colon.
print(line)