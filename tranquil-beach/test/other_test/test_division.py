import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.division import Division

class TestDivision(unittest.TestCase):
    def setUp(self):
        self.func = Division()

    def test_1(self):
        dividend, divisor = 10, 3
        expected = 3
        self.assertEqual(self.func.divide(dividend, divisor), expected)

    def test_2(self):
        dividend, divisor = 7, -3
        expected = -2
        self.assertEqual(self.func.divide(dividend, divisor), expected)

    def test_3(self):
        dividend, divisor = -2147483648, -1
        expected = 2147483647
        self.assertEqual(self.func.divide(dividend, divisor), expected)

if __name__ == '__main__':
    unittest.main()