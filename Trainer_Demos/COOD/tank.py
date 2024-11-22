#! /usr/bin/env python3
# Author: DCameron
# Description: This module describes a Tank class.
"""
    A Class of Tank for online game.
"""
import vehicle

class Tank(vehicle.Vehicle):
    # Attributes/Data and Behaviour/Methods
    def __init__(self, country, model):
        vehicle.Vehicle.__init__(self, country, model)
        self._direction = 0
        self._location = {'x': 0, 'y': 0, 'z': 0}
        self._shells = 20
        self._health = 100
        # No EXPLICIT return as its called implicitly.

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    # Some Special Methods..
    # Example of OPERATOR overloading
    def __add__(self, other):
        return self._health + other._health

    # EXample of a GETTER and a SETTER method
    def get_health(self):
        return self._health

    def set_health(self, newhealth):
        self._health = newhealth
        return None

    # WRAP ONE variable name interface to multiple methods.
    # tank_health = property(get_health, set_health)

    # Alternative way of wrapping a function on another function to
    # give additional properties USING decorators..
    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    def tank_health(self, newhealth):
        self._health = newhealth
        return None

    # Example of DUCK TYPING, a Tank can NOW QUACK LIKE A STR!
    def __str__(self):
        return f"Model={self.model}, Health={self._health}, Speed={self._speed}"


