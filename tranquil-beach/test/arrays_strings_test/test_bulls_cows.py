import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.bulls_cows import BullsCows

class TestBullsCows(unittest.TestCase):
    def setUp(self):
        self.func = BullsCows().getHint

    def test_1(self):
        secret, guess = '1807', '7810'
        expected = '1A3B'
        self.assertEqual(expected, self.func(secret, guess))

    def test_2(self):
        secret, guess = '1123', '0111'
        expected = '1A1B'
        self.assertEqual(expected, self.func(secret, guess))

    def test_3(self):
        secret, guess = "1122", "1222"
        expected = "3A0B"
        self.assertEqual(expected, self.func(secret, guess))

if __name__ == '__main__':
    unittest.main()
