import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.rotated_sorted_array_with_dup import RotatedSortedArrayWithDup

class TestRotatedSortedArrayWithDup(unittest.TestCase):
    def setUp(self):
        self.func = RotatedSortedArrayWithDup()

    def test_1(self):
        nums = [2,5,6,0,0,1,2]
        target = 0
        self.assertTrue(self.func.search(nums, target))

    def test_2(self):
        nums = [2,5,6,0,0,1,2]
        target = 3
        self.assertFalse(self.func.search(nums, target))

if __name__ == '__main__':
    unittest.main()