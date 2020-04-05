import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.stock_multiple import StockMultiple

class TestStock(unittest.TestCase):
    def setUp(self):
        self.func = StockMultiple().maxProfit

    def test_1(self):
        input = [7,1,5,3,6,4]
        expected = 7
        self.assertEqual(self.func(input), expected)

    def test_2(self):
        input = [1,2,3,4,5]
        expected = 4
        self.assertEqual(self.func(input), expected)

    def test_3(self):
        input = [7,6,4,3,1]
        expected = 0
        self.assertEqual(self.func(input), expected)

if __name__ == '__main__':
    unittest.main()