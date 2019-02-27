import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.subarray_sum_k import SubarraySumK

class TestSubarraySumK(unittest.TestCase):
    def setUp(self):
        self.func = SubarraySumK()

    def test_1(self):
        nums = [1, 1, 1]
        k = 2
        expected = 2
        self.assertEqual(self.func.subarraySum(nums, k), expected)

    def test_2(self):
        nums = [1,2,1,2,1]
        k = 3
        expected = 4
        self.assertEqual(self.func.subarraySum(nums, k), expected)

if __name__ == '__main__':
    unittest.main()