import unittest
from triangle import classify_triangle

class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral')

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles')

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene')

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene')

    def test_invalid(self):
        self.assertEqual(classify_triangle(-1, 2, 2), 'Invalid Input')
        self.assertEqual(classify_triangle(0, 0, 0), 'Invalid Input')
        self.assertEqual(classify_triangle(1, 1, 2), 'Not a Triangle')

if __name__ == '__main__':
    unittest.main()
