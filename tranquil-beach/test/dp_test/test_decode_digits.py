import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.decode_digits import DecodeDigits

class TestDecodeDigits(unittest.TestCase):
    def setUp(self):
        self.func = DecodeDigits()

    def test_1(self):
        s = "12"
        expected = 2
        self.assertEqual(self.func.numDecodings(s), expected)

    def test_2(self):
        s = "226"
        expected = 3
        self.assertEqual(self.func.numDecodings(s), expected)

if __name__ == '__main__':
    unittest.main()
