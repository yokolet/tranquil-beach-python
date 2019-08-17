import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.multiply import Multiply

class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.func = Multiply().multiply

    def test_1(self):
        num1, num2 = '2', '3'
        expected = '6'
        self.assertEqual(expected, self.func(num1, num2))

    def test_2(self):
        num1, num2 = '123', '456'
        expected = '56088'
        self.assertEqual(expected, self.func(num1, num2))

if __name__ == '__main__':
    unittest.main()