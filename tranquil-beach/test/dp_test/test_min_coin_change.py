import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.min_coin_change import MinCoinChange

class TestMinCoinChange(unittest.TestCase):
    def setUp(self):
        self.func = MinCoinChange()

    def test_1(self):
        coins = [1, 2, 5]
        amount = 11
        expected = 3
        self.assertEqual(self.func.coinChange(coins, amount), expected)

    def test_2(self):
        coins = [2]
        amount = 3
        expected = -1
        self.assertEqual(self.func.coinChange(coins, amount), expected)

if __name__ == '__main__':
    unittest.main()
