import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.strobogrammatic_len_n import StrobogrammaticLenN

class TestStrobogrammaticLenN(unittest.TestCase):
    def setUp(self):
        self.func = StrobogrammaticLenN().findStrobogrammatic

    def test_1(self):
        n = 2
        expected = ["11","69","88","96"]
        self.assertEqual(expected, self.func(n))

    def test_2(self):
        n = 1
        expected = ['0', '1', '8']
        self.assertEqual(expected, self.func(n))

if __name__ == '__main__':
    unittest.main()
