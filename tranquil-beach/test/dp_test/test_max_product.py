import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.max_product import MaxProduct

class TestMaxProduct(unittest.TestCase):
    def setUp(self):
        self.func = MaxProduct().maxProduct

    def test_1(self):
        nums = [2,3,-2,4]
        expected = 6
        self.assertEqual(expected, self.func(nums))

    def test_2(self):
        nums = [-2,0,-1]
        expected = 0
        self.assertEqual(expected, self.func(nums))

if __name__ == '__main__':
    unittest.main()