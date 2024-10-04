# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classifyTriangle

class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral')

    def test_isosceles(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles')

    def test_scalene(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    def test_right_triangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right Scalene')

    def test_invalid(self):
        self.assertEqual(classifyTriangle(-1, 2, 2), 'Invalid Input')
        self.assertEqual(classifyTriangle(0, 0, 0), 'Invalid Input')
        self.assertEqual(classifyTriangle(1, 1, 2), 'Not a Triangle')

if __name__ == '__main__':
    unittest.main()

