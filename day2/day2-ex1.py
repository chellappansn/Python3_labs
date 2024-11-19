#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Lotto

"""
   Docstring
"""

import random
lotto = []

while len(lotto) < 6:
    num = random.randint(1,50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number: ", num)

print("Lotto number", lotto)
