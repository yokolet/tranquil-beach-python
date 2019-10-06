import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.largest_number import LargestNumber

class TestLargestNumber(unittest.TestCase):
    def setUp(self):
        self.func = LargestNumber().largestNumber

    def test_1(self):
        nums = [10,2]
        expected = '210'
        self.assertEqual(expected, self.func(nums))

    def test_2(self):
        nums = [3,30,34,5,9]
        expected = '9534330'
        self.assertEqual(expected, self.func(nums))

    def test_3(self):
        nums = [0,0]
        expected = '0'
        self.assertEqual(expected, self.func(nums))

if __name__ == '__main__':
    unittest.main()