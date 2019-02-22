import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.arranging_coins import Coins

class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.func = Coins()

    def test_1(self):
        n = 5
        expected = 2
        self.assertEqual(self.func.arrangeCoins(n), expected)

    def test_2(self):
        n = 8
        expected = 3
        self.assertEqual(self.func.arrangeCoins(n), expected)

if __name__ == '__main__':
    unittest.main()