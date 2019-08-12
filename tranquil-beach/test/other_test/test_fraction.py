import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.fraction import Fraction

class TestFraction(unittest.TestCase):
    def setUp(self):
        self.func = Fraction().fractionToDecimal

    def test_1(self):
        numerator, denominator = 1, 2
        expected = '0.5'
        self.assertEqual(expected, self.func(numerator, denominator))

    def test_2(self):
        numerator, denominator = 2, 1
        expected = '2'
        self.assertEqual(expected, self.func(numerator, denominator))

    def test_3(self):
        numerator, denominator = 2, 3
        expected = '0.(6)'
        self.assertEqual(expected, self.func(numerator, denominator))

    def test_4(self):
        numerator, denominator = 4, 333
        expected = '0.(012)'
        self.assertEqual(expected, self.func(numerator, denominator))

    def test_5(self):
        numerator, denominator = 0, 3
        expected = '0'
        self.assertEqual(expected, self.func(numerator, denominator))

if __name__ == '__main__':
    unittest.main()