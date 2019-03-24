import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.max_sum_3 import MaxSum3

class TestMaxSum3(unittest.TestCase):
    def setUp(self):
        self.func = MaxSum3()

    def test_1(self):
        nums, k = [1,2,1,2,6,7,5,1], 2
        expected = [0, 3, 5]
        self.assertEqual(self.func.maxSumOfThreeSubarrays(nums, k), expected)

if __name__ == '__main__':
    unittest.main()