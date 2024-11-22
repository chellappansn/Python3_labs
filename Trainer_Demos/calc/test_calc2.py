#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import unittest
import basic

class Testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(4, 3), 7.0, "Error should be 7.0")
        self.assertEqual(basic.add(4, 3, 2), 9.0, "Error should be 9.0")
        return None

    def test_mul(self):
        self.assertEqual(basic.mul(4, 3), 12.0, "Error should be 12.0")
        self.assertEqual(basic.mul(4, 3, 2), 24.0, "Error should be 24.0")
        return None

    def test_div(self):
        self.assertEqual(basic.div(4, 3), 1.333, "Error should be 1.333")
        return None

if __name__ == "__main__":
    unittest.main()