import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.sorted_arrays_median import SotredArraysMedian

class TestSortedArraysMedian(unittest.TestCase):
    def setUp(self):
        self.func = SotredArraysMedian().findMedianSortedArrays

    def test_1(self):
        nums1, nums2 = [1, 3], [2]
        expected = 2.0
        self.assertEquals(expected, self.func(nums1, nums2))

    def test_2(self):
        nums1, nums2 = [1, 2], [3, 4]
        expected = 2.5
        self.assertEquals(expected, self.func(nums1, nums2))

if __name__ == '__main__':
    unittest.main()