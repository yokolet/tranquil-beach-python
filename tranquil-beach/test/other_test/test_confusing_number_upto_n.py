import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.confusing_number_upto_n import ConfusingNumberUptoN

class TestConfusingNumberUptoN(unittest.TestCase):
    def setUp(self):
        self.func = ConfusingNumberUptoN().confusingNumberII

    def test_1(self):
        N = 20
        expected = 6
        self.assertEqual(self.func(N), expected)

    def test_2(self):
        N = 100
        expected = 19
        self.assertEqual(self.func(N), expected)

if __name__ == '__main__':
    unittest.main()
