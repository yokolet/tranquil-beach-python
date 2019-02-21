import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.kth_largest import KthLargest

class TestTreePath(unittest.TestCase):
    def setUp(self):
        self.func = KthLargest()

    def test_1(self):
        nums = [3,2,1,5,6,4]
        k = 2
        expected = 5
        self.assertEqual(self.func.findKthLargest(nums, k), expected)

    def test_2(self):
        nums = [3,2,3,1,2,4,5,5,6]
        k = 4
        expected = 4
        self.assertEqual(self.func.findKthLargest(nums, k), expected)

if __name__ == '__main__':
    unittest.main()