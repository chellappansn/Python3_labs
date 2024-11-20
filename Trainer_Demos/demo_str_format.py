#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo different wasy of formatting strings
# using str concatenation and escape chars, str justification methods, the
# str format() method and f-strings (Py 3.5)!
"""
    Docstring:
"""
# Dict of planets and their distance to the SUN in Gigametres.
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# ITERATE through the dict keys and Format planetary info
# using str concatenation and escape chars. UGLY!
for planet in planets:
    print("\t\t" + planet + ": \t" + str(planets[planet]) + " Gm\t" + str(hex(0xff)))

print("-" * 60)
# using str justification methods. OK!
for planet in planets:
    print(planet.rjust(12) + ":" + str(planets[planet]).rjust(12) + " Gm " + str(hex(0xff)).rjust(6))

print("-" * 60)
# using str .format() method. Python 3 - GOOD!
for planet in planets:
    print("{0:>12s}: {1:>12.3f} Gm {2:#6x}".format(planet, planets[planet], 0xff))

print("-" * 60)
# using f-strings (from Python 3.5 onwards) - My favourite!
for planet in planets:
    print(f"{planet:>12s}: {planets[planet]:>12.3f} Gm {0xff:#6x}")