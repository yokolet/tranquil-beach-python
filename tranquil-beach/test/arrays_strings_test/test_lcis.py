import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.lcis import Lcis

class TestLcis(unittest.TestCase):
    def setUp(self):
        self.func = Lcis()

    def test_1(self):
        nums = [1,3,5,4,7]
        expected = 3
        self.assertEqual(self.func.findLengthOfLCIS(nums), expected)

    def test_2(self):
        nums = [2,2,2,2,2]
        expected = 1
        self.assertEqual(self.func.findLengthOfLCIS(nums), expected)

if __name__ == '__main__':
    unittest.main()