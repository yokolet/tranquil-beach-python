import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.missing_ranges import MissingRanges

class TestMissingRanges(unittest.TestCase):
    def setUp(self):
        self.func = MissingRanges().findMissingRanges

    def test_1(self):
        nums, lower, upper = [0, 1, 3, 50, 75], 0, 99
        expected = ["2", "4->49", "51->74", "76->99"]
        self.assertEqual(expected, self.func(nums, lower, upper))

    def test_2(self):
        nums, lower, upper = [], 1, 1
        expected = ["1"]
        self.assertEqual(expected, self.func(nums, lower, upper))

if __name__ == '__main__':
    unittest.main()