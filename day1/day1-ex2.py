#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Ex 2

import showcard

number = input("Pick a card(1-52): ")

filename = "BMP" + number + ".GIF"
showcard.display_file(filename)
