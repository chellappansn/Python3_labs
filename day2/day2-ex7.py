#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: String manipulation

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

city = Belgium.replace(",", ":")
print("Replaced , with : - ", city)

lscity = Belgium.split(",")
print(lscity)
population = int(lscity[1]) + int(lscity[3])
print("Total population of Belgium and Brussels: ", population)

print("-" * len(Belgium))
print(':'.join(lscity))
print(int(lscity[1]) + int(lscity[3]))
print("-" * len(Belgium))