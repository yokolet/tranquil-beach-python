import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.roman_to_integer import RomanToInteger

class TestRomanToInteger(unittest.TestCase):
    def setUp(self):
        self.func = RomanToInteger()

    def test_1(self):
        s = "III"
        expected = 3
        self.assertEqual(self.func.romanToInt(s), expected)

    def test_2(self):
        s = "IV"
        expected = 4
        self.assertEqual(self.func.romanToInt(s), expected)

    def test_3(self):
        s = "IX"
        expected = 9
        self.assertEqual(self.func.romanToInt(s), expected)

    def test_4(self):
        s = "LVIII"
        expected = 58
        self.assertEqual(self.func.romanToInt(s), expected)

    def test_5(self):
        s = "MCMXCIV"
        expected = 1994
        self.assertEqual(self.func.romanToInt(s), expected)

if __name__ == '__main__':
    unittest.main()