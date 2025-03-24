import unittest
import math
from circle import Circle

class TestCircle(unittest.TestCase):

    def test_area(self):
        circle = Circle(3)
        expected_area = round(math.pi * 3 ** 2, 2)
        self.assertEqual(circle.area(), expected_area)

    def test_perimeter(self):
        circle = Circle(3)
        expected_perimeter = round(2 * math.pi * 3, 2)
        self.assertEqual(circle.perimeter(), expected_perimeter)

if __name__ == '__main__':
    unittest.main()