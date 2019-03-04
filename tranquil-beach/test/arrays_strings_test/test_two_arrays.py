import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.two_arrays import TwoArrays

class TestTwoArrays(unittest.TestCase):
    def setUp(self):
        self.func = TwoArrays()

    def test_1(self):
        nums1, nums2 = [1,2,2,1], [2,2]
        expected = [2,2]
        self.assertEqual(self.func.intersect(nums1, nums2), expected)

    def test_2(self):
        nums1, nums2 = [4,9,5], [9,4,9,8,4]
        expected = [4,9]
        self.assertEqual(self.func.intersect(nums1, nums2), expected)

if __name__ == '__main__':
    unittest.main()