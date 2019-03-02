import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.reverse_integer import ReverseInteger

class TestReverseInteger(unittest.TestCase):
    def setUp(self):
        self.func = ReverseInteger()

    def test_1(self):
        x = 123
        expected = 321
        self.assertEqual(self.func.reverse(x), expected)

    def test_2(self):
        x = -123
        expected = -321
        self.assertEqual(self.func.reverse(x), expected)

    def test_3(self):
        x = 120
        expected = 21
        self.assertEqual(self.func.reverse(x), expected)

if __name__ == '__main__':
    unittest.main()