#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo howto define, name, and call a user function
# with optional parameter passing and return values.
"""
    Docstring:
"""
# Example of a user function with optional parameter passing
# and default values. Use annotations to describe the data type
# expected for the parameters.
def say_hello(greeting:str="ciao", recipient:str="amici")->None:
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_hello("bonjour", "mes amis") # Positional parameter passing.
say_hello(greeting="mabuhay", recipient="kibigan") # Named parameter passing.
say_hello(recipient="amigos", greeting="hola") # Named parameter passing in different order.
say_hello("ciao", recipient="amici") # Mixed parameter passing (optional->named).
say_hello()


print(f"Annotations for say_hello: {say_hello.__annotations__}") # Fact finding.