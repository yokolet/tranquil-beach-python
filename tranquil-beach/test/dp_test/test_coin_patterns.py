import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.coin_patterns import CoinPatterns

class TestCoinPatterns(unittest.TestCase):
    def setUp(self):
        self.func = CoinPatterns()

    def test_0(self):
        amount = 0
        coins = []
        expected = 1
        self.assertEqual(self.func.change(amount, coins), expected)

    def test_1(self):
        amount = 5
        coins = [1, 2, 5]
        expected = 4
        self.assertEqual(self.func.change(amount, coins), expected)

    def test_2(self):
        amount = 3
        coins = [2]
        expected = 0
        self.assertEqual(self.func.change(amount, coins), expected)

    def test_3(self):
        amount = 10
        coins = [10]
        expected = 1
        self.assertEqual(self.func.change(amount, coins), expected)

if __name__ == '__main__':
    unittest.main()
