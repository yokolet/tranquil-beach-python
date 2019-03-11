import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.subarray_sum_nk import SubarraySumNK

class TestSubarraySumNK(unittest.TestCase):
    def setUp(self):
        self.func = SubarraySumNK()

    def test_1(self):
        nums, k = [23, 2, 4, 6, 7], 6
        self.assertTrue(self.func.checkSubarraySum(nums, k))

    def test_2(self):
        nums, k = [23, 2, 6, 4, 7], 6
        self.assertTrue(self.func.checkSubarraySum(nums, k))

    def test_3(self):
        nums, k = [0, 0], 0
        self.assertTrue(self.func.checkSubarraySum(nums, k))

    def test_4(self):
        nums, k = [0,1,0], 0
        self.assertFalse(self.func.checkSubarraySum(nums, k))

if __name__ == '__main__':
    unittest.main()
