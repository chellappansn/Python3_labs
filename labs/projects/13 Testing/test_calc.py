#! /usr/bin/env python3
# Name:        .py
# Author:      Donald Cameron
# Revision:    v1.0
# Description: This program 
"""
    DocString:
"""
from calculator import demo_calc

def test_add():
    assert demo_calc.add(4, 3) == 7, "Error should return 7"
    assert demo_calc.add(10, 20, 30) == 50, "Error should return 60"
    return None

def test_mul():
    assert demo_calc.mul(4, 3) == 12, "Error should return 12"
    return None

def test_div():
    assert demo_calc.div(4, 3), "Error should return '1.333'"
    return None

def test_div_zero():
    assert demo_calc.div(4, 3) == 1.333, "Error should return '1.333'"
    return None

def main():
    """ Execute Test functions """
    test_add()
    test_mul()
    test_div()
    # test_div_zero()
    print("Everything passed")
    return None

if __name__ == "__main__":
    main()