import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.next_permutation import NextPermutation

class TestNextPermutation(unittest.TestCase):
    def setUp(self):
        self.func = NextPermutation()

    def test_1(self):
        nums = [1,2,3]
        expected = [1,3,2]
        self.func.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_2(self):
        nums = [3,2,1]
        expected = [1,2,3]
        self.func.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_3(self):
        nums = [1,1,5]
        expected = [1,5,1]
        self.func.nextPermutation(nums)
        self.assertEqual(nums, expected)

if __name__ == '__main__':
    unittest.main()