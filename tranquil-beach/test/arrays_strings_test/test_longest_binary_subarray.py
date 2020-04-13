import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.longest_binary_subarray import LongestBinarySubarray

class TestLongestBinarySubarray(unittest.TestCase):
    def setUp(self):
        self.func = LongestBinarySubarray().findMaxLength

    def test_1(self):
        nums = [0,1]
        expected = 2
        self.assertEqual(expected, self.func(nums))

    def test_2(self):
        nums = [0,1,0]
        expected = 2
        self.assertEqual(expected, self.func(nums))

    def test_3(self):
        nums = [1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,
                1,0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0]
        expected = 86
        self.assertEqual(expected, self.func(nums))

if __name__ == '__main__':
    unittest.main()
