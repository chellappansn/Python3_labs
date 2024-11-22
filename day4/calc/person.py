
#! /usr/bin/env python3
# Author: Chellappan Sampath
# Version: 1.0
# Description: Person - name, age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def inage(self, iage):
        self.age += iage
        return None

    def deage(self, dage):
        self.age -= dage
        return None

    # Operator overloading
    def __add__(self, other):
        return self.age + other.age

    # Option 1 - Getter and Setter for an attribute
    def getage(self):
        return self.age

    def setage(self, age):
        self.age = age
        return None

    # Wrap one variable name interface to multiple methods
    personage = property(getage, setage)

    # Option 2 - Using annotation property
    @property
    def personname(self):
        return self.name

    @personname.setter
    def personname(self, name):
        self.name = name
        return name

    def __str__(self):
        return f"Name={self.name} Age={self.age}"