import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.lis import LIS

class TestCoinPatterns(unittest.TestCase):
    def setUp(self):
        self.func = LIS()

    def test_1(self):
        nums = [10,9,2,5,3,7,101,18]
        expected = 4
        self.assertEqual(self.func.lengthOfLIS(nums), expected)

if __name__ == '__main__':
    unittest.main()
