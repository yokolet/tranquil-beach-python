import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.confusing_number import ConfusingNumber

class TestConfusingNumber(unittest.TestCase):
    def setUp(self):
        self.func = ConfusingNumber().confusingNumber

    def test_1(self):
        N = 6
        self.assertTrue(self.func(N))

    def test_2(self):
        N = 89
        self.assertTrue(self.func(N))

    def test_3(self):
        N = 11
        self.assertFalse(self.func(N))

    def test_4(self):
        N = 25
        self.assertFalse(self.func(N))

if __name__ == '__main__':
    unittest.main()
