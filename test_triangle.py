import unittest
from Triangle_problem import classify_triangle  # Ensure correct import

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral Triangle")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles Triangle")
    
    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right Triangle")
    
    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(0, 2, 3), "Invalid Triangle")
    
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(6, 8, 10), "Scalene and Right Triangle")

    # Additional edge case test: Negative side length
    def test_negative_side(self):
        self.assertEqual(classify_triangle(-3, 4, 5), "Invalid Triangle")


if __name__ == '__main__':
    unittest.main()
