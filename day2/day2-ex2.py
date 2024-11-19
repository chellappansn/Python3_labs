#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: This script will simulate a high stree back PIN machine

"""
   Docstring
"""

master_pin = "0123"
pin = None

while pin != master_pin:
    pin = input("Enter PIN:")

    if pin == master_pin:
        print("Valid PIN")
    else:
        print("Invalid PIN ", pin)

print("Done.")