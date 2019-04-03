import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.intersection import Intersection

class TestIntersection(unittest.TestCase):
    def setUp(self):
        self.func = Intersection()

    def test_1(self):
        nums1, nums2 = [1,2,2,1], [2,2]
        expected = [2]
        self.assertEqual(self.func.intersection(nums1, nums2), expected)

    def test_2(self):
        nums1, nums2 = [4,9,5], [9,4,9,8,4]
        expected = [9, 4]
        self.assertCountEqual(self.func.intersection(nums1, nums2), expected)

if __name__ == '__main__':
    unittest.main()