import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.consecutive_k_numbers import ConsecutiveKNumbers

class TestConsecutiveKNumbers(unittest.TestCase):
    def setUp(self):
        self.func = ConsecutiveKNumbers().isPossibleDivide

    def test_1(self):
        nums, k = [1,2,3,3,4,4,5,6], 4
        self.assertTrue(self.func(nums, k))

    def test_2(self):
        nums, k = [3,2,1,2,3,4,3,4,5,9,10,11], 3
        self.assertTrue(self.func(nums, k))

    def test_3(self):
        nums, k = [3,3,2,2,1,1], 3
        self.assertTrue(self.func(nums, k))

    def test_4(self):
        nums, k = [1,2,3,4], 3
        self.assertFalse(self.func(nums, k))

    def test_5(self):
        nums, k = [1,3,4,6], 4
        self.assertFalse(self.func(nums, k))

if __name__ == '__main__':
    unittest.main()
