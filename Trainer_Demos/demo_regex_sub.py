#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO match and SUBSTITUTE patterns using
# re.sub() and re.subn() functions.
"""
    Docstring:
"""
import re

# Sample line from /etc/passwd on Linux for the root user login.
line = "root:x:0:0:The Super User:/root:/bin/ksh"
line = re.sub(r"[sS]uper [uU]ser", r"Administrator", line) # Return modified str.
(line, num) = re.subn(r"ksh$", r"bash", line) # Return TUPLE (modified str, num changes)

print(f"Modified line={line} with {num} changes")