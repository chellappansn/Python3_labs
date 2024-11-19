#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: File manipulation

for line in open('C:\\Users\\Admin\\Labs_DC\\Python3_labs\\labs\\messier.txt', encoding='latin_1'):
    if not line:
        break
    if line.startswith('M'):
        mnumber = line[:6].rstrip()
        comname = line[6:40].rstrip()
        if not comname:
            comname = 'no name'
        otype = line[40:64].rstrip()
        oconst = line[64:].rstrip()
        print(f"|{mnumber}|{comname}|{otype}|{oconst}")

