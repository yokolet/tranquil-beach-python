import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.sorted_array import SortedArray

class TestSortedArray(unittest.TestCase):
    def setUp(self):
        self.func = SortedArray()

    def test_1(self):
        nums1, m = [1,2,3,0,0,0], 3
        nums2, n = [2,5,6], 3
        expected = [1,2,2,3,5,6]
        self.func.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

if __name__ == '__main__':
    unittest.main()