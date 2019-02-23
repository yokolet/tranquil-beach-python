import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.stock import Stock

class TestStock(unittest.TestCase):
    def setUp(self):
        self.func = Stock()

    def test_1(self):
        input = [7,1,5,3,6,4]
        expected = 5
        self.assertEqual(self.func.maxProfit(input), expected)

    def test_2(self):
        input = [7,6,4,3,1]
        expected = 0
        self.assertEqual(self.func.maxProfit(input), expected)

if __name__ == '__main__':
    unittest.main()
