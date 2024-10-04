# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):
    # Check for invalid input
    if a <= 0 or b <= 0 or c <= 0:
        return 'Invalid Input'
    # Check for triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'Not a Triangle'
    # Classify triangle
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        return 'Right Scalene'
    else:
        return 'Scalene'