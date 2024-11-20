#! /usr/bin/env python3
# Name:        .py
# Author:      Donald Cameron
# Revision:    v1.0
# Description: This program will demo unit testing and test runners.
"""
    DocString:
"""

import unittest
from calculator import demo_calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(demo_calc.add(4, 3), 7, "Error, should be 7")
        self.assertEqual(demo_calc.add(4.2, 3.5), 7.7, "Error, should be 8.7")
        return None

    def test_mul(self):
        self.assertEqual(demo_calc.mul(4, 3), 12, "Error, should be 12")
        self.assertEqual(demo_calc.mul(102, 3, -2), -612, "Error, should be -612")
        return None

    def test_div(self):
        self.assertEqual(demo_calc.div(4, 3), 1.3333, "Error, should be 1.333")
        return None

    def test_div_zero(self):
        self.assertRaises(ZeroDivisionError, demo_calc.div, 4, 0)
        return None

if __name__ == "__main__":
    unittest.main()