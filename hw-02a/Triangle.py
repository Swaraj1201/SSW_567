# -*- coding: utf-8 -*-
"""
This module provides a function to classify triangles based on the lengths of their sides.
"""

def classify_triangle(side_a, side_b, side_c):
    """
    Classifies a triangle based on the lengths of its sides.

    :param side_a: Length of side A
    :param side_b: Length of side B
    :param side_c: Length of side C
    :return: Type of triangle as a string
    """
    # Check for invalid input
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'Invalid Input'
    # Check for triangle inequality
    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        return 'Not a Triangle'
    # Classify triangle
    if side_a == side_b == side_c:
        return 'Equilateral'
    if side_a == side_b or side_b == side_c or side_a == side_c:
        return 'Isosceles'
    if (side_a**2 + side_b**2 == side_c**2) or \
       (side_b**2 + side_c**2 == side_a**2) or \
       (side_c**2 + side_a**2 == side_b**2):
        return 'Right Scalene'
    return 'Scalene'

