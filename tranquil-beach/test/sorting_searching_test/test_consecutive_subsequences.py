import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.consecutive_subsequences import ConsecutiveSubsequences

class TestConsecutiveSubsequences(unittest.TestCase):
    def setUp(self):
        self.func = ConsecutiveSubsequences().isPossible

    def test_1(self):
        nums = [1,2,3,3,4,5]
        self.assertTrue(self.func(nums))

    def test_2(self):
        nums = [1,2,3,3,4,4,5,5]
        self.assertTrue(self.func(nums))

    def test_3(self):
        nums = [1,2,3,4,4,5]
        self.assertFalse(self.func(nums))

    def test_4(self):
        nums = [1,2,3,4,6,7,8,9,10,11]
        self.assertTrue(self.func(nums))

    def test_5(self):
        from test_consecutive_subsequences_data import nums
        self.assertTrue(self.func(nums))

if __name__ == '__main__':
    unittest.main()
