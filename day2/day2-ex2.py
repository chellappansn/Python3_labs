#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: This script will simulate a high stree back PIN machine

"""
   Docstring
"""

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter PIN:")

    if pin == master_pin:
        print("Valid PIN")
        break # Breaks the entire loop
    else:
        print("Invalid PIN ", pin)

    attempts += 1
    print("Attempts: ", attempts)
else:
    # Execute only once when condition becomes False
    print("Too many attempts")

print("Done.")