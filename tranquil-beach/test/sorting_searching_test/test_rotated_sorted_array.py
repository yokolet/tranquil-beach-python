import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.rotated_sorted_array import RotatedSortedArray

class TestRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.func = RotatedSortedArray()

    def test_1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        expected = 4
        self.assertEqual(self.func.search(nums, target), expected)

    def test_2(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        expected = -1
        self.assertEqual(self.func.search(nums, target), expected)

    def test_3(self):
        nums = []
        target = 5
        expected = -1
        self.assertEqual(self.func.search(nums, target), expected)

    def test_4(self):
        nums = [1]
        target = 0
        expected = -1
        self.assertEqual(self.func.search(nums, target), expected)

    def test_5(self):
        nums = [1,3]
        target = 1
        expected = 0
        self.assertEqual(self.func.search(nums, target), expected)

    def test_6(self):
        nums = [3,1]
        target = 1
        expected = 1
        self.assertEqual(self.func.search(nums, target), expected)

    def test_7(self):
        nums = [5,1,3]
        target = 2
        expected = -1
        self.assertEqual(self.func.search(nums, target), expected)

if __name__ == '__main__':
    unittest.main()