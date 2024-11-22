#! /usr/bin/env python3
# Author: DCameron
# Description: This is an ultra realistic online games with Tanks!
"""
    GOT - Game of Tanks
"""
import sys
import tank

def main():
    # Create/Instantiate 3 new Tank objects
    thomas_tank = tank.Tank("german", "tiger")
    rick_tank = tank.Tank("american", "sherman")
    rajat_tank = tank.Tank("british", "churchill")

    # And the game begins..
    thomas_tank.accel(39)
    rick_tank.accel(28)

    rajat_tank.rotate_left(289)
    rajat_tank.accel(31)
    rajat_tank.shoot()

    # and success..
    thomas_tank.take_damage(62)
    rick_tank.take_damage(22)

    # And now for some visuals, or at least some print statements!
    # print(f"Thomas's tank has health of {thomas_tank._health}") # POOR CODE!

    # Example of OPERATOR overloading
    print(f"Status of Thomas's and Rick's Tank = {thomas_tank + rick_tank}")

    print(f"Status of Thomas's Tank is {thomas_tank}")

    # Thomas has just obtained a HEALTH boost!
    # thomas_tank._health = 100 # Never ACCESS a PRIVATE variable directly!
    # print(f"New health of Thomas's tank is {thomas_tank._health}")
    thomas_tank.set_health(101) # SETTER method :-)
    print(f"New health of Thomas's tank is {thomas_tank.get_health()}") # GETTER method :-)

    thomas_tank.tank_health = 102 # SETTER method :-)
    print(f"New health of Thomas's tank is {thomas_tank.tank_health}") # GETTER method :-)

    return None

# Namespace Trick
if __name__ == "__main__":
    main()
    sys.exit(0)