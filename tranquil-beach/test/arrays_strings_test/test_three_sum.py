import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.three_sum import ThreeSum

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.func = ThreeSum().threeSum

    def test_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, 0, 1],[-1, -1, 2]]
        self.assertCountEqual(expected, self.func(nums))

if __name__ == '__main__':
    unittest.main()