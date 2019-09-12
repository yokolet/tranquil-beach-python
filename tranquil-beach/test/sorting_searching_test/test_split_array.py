import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.split_array import SplitArray

class TestSplitArray(unittest.TestCase):
    def setUp(self):
        self.func = SplitArray().splitArray

    def test_1(self):
        nums, m = [7,2,5,10,8], 2
        expected = 18
        self.assertEqual(expected, self.func(nums, m))

    def test_2(self):
        nums, m = [7,6,5,4,3,2,1], 2
        expected = 15
        self.assertEqual(expected, self.func(nums, m))

if __name__ == '__main__':
    unittest.main()