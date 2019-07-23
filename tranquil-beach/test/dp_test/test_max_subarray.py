import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.max_subarray import MaxSubarray

class TestMaxSubarray(unittest.TestCase):
    def setUp(self):
        self.func = MaxSubarray().maxSubArray

    def test_1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        expected = 6
        self.assertEquals(expected, self.func(nums))

if __name__ == '__main__':
    unittest.main()