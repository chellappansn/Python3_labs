#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Lotto

"""
   Random generate lotto number
"""

import random
lotto = []

while len(lotto) < 10:
    num = random.randint(1,50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number: ", num)

print("Lotto number", lotto)

if 5 in lotto:
    print ("Five exists")
else:
    print("Five does not exists")

