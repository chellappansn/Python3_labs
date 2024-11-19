#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Day1 Ex2

from math import pi, tan, cos
g = 9.81
v0 = 44
theta = 80 * (pi/180)
x = 0.5
y0 = 1

y = y0 + x*tan(theta) - (g * x**2)/(2 * ((v0 * cos(theta))**2))

print('Height:', y, 'm')

