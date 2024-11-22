#! /usr/bin/env python3
# Author: DCameron
# Description: TEST Cases for calculator App.
"""
    Docstring:
"""
import basic

def test_add():
    assert basic.add(4, 3) == 7.0, "Error should be 7.0"
    assert basic.add(4, 3, 2) == 9.1, "Error should be 9.0"
    return None

def test_mul():
    assert basic.mul(4, 3) == 12.0, "Error should be 12.0"
    assert basic.mul(4, 3, 2) == 24.1, "Error should be 24.0"
    return None

def test_div():
    assert basic.div(4, 3) == 1.334, "Error should be 1.333"
    return None

def main():
    print("Starting Test Cases..")
    test_add()
    test_mul() # ONLY FINDS FIRST TEST ERROR! NEED TEST RUNNER to FIND ALL
    test_div()
    print("All tests PASSED")
    return None

if __name__ == "__main__":
    main()