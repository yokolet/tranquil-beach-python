import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.median_of_arrays import MedianOfArrays

class TestMedianOfArrays(unittest.TestCase):
    def setUp(self):
        self.func = MedianOfArrays()

    def test_1(self):
        nums1, nums2 = [1, 3], [2]
        expected = 2.0
        self.assertEqual(self.func.findMedianSortedArrays(nums1, nums2), expected)

    def test_2(self):
        nums1, nums2 = [1, 2], [3, 4]
        expected = 2.5
        self.assertEqual(self.func.findMedianSortedArrays(nums1, nums2), expected)

if __name__ == '__main__':
    unittest.main()