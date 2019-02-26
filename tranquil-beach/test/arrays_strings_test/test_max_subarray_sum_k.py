import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.max_subarray_sum_k import MaxSubarraySumK

class TestMaxSubarraySumK(unittest.TestCase):
    def setUp(self):
        self.func = MaxSubarraySumK()

    def test_1(self):
        nums = [1, -1, 5, -2, 3]
        k = 3
        expected = 4
        self.assertEqual(self.func.maxSubArrayLen(nums, k), expected)
    
    def test_2(self):
        nums = [-2, -1, 2, 1]
        k = 1
        expected = 2
        self.assertEqual(self.func.maxSubArrayLen(nums, k), expected)
    

if __name__ == '__main__':
    unittest.main()