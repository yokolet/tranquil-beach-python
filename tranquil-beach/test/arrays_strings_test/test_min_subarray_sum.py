import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.min_subarray_sum import MinSubarraySum

class TestMinSubarraySum(unittest.TestCase):
    def setUp(self):
        self.func = MinSubarraySum()

    def test_1(self):
        s = 7
        nums = [2,3,1,2,4,3]
        expected = 2
        self.assertEqual(self.func.minSubArrayLen(s, nums), expected)

if __name__ == '__main__':
    unittest.main()