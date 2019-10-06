import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.arithmetic_calculator import ArithmeticCalculator

class TestArithmeticCalculator(unittest.TestCase):
    def setUp(self):
        self.func = ArithmeticCalculator().calculate

    def test_1(self):
        s = '3+2*2'
        expected = 7
        self.assertEqual(expected, self.func(s))

    def test_2(self):
        s = ' 3/2 '
        expected = 1
        self.assertEqual(expected, self.func(s))

    def test_3(self):
        s = ' 3+5 / 2 '
        expected = 5
        self.assertEqual(expected, self.func(s))

    def test_4(self):
        s = '14-3/2'
        expected = 13
        self.assertEqual(expected, self.func(s))

if __name__ == '__main__':
    unittest.main()