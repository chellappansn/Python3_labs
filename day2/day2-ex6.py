#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Print files in home directory

"""
   Docstring
"""

import os
import sys
import glob

# Get the directory name

if sys.platform == "win32":
    dir = os.environ["HOMEPATH"] # Get homepath
else:
    dir = os.environ["HOME"]
print (dir)

pattern = os.path.join(dir, "*")
print (pattern)

for fname in glob.glob(pattern):
    size = os.path.getsize(fname)
    if size > 0:
        print(os.path.basename(fname), size/1024 + "MB")

