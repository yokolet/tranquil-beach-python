import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.longest_substring_2_distinct import LongestSubstring2Distinct

class TestLongestSubstring2Distinct(unittest.TestCase):
    def setUp(self):
        self.func = LongestSubstring2Distinct().lengthOfLongestSubstringTwoDistinct

    def test_1(self):
        s = 'eceba'
        expected = 3
        self.assertEqual(expected, self.func(s))

    def test_2(self):
        s = 'ccaabbb'
        expected = 5
        self.assertEqual(expected, self.func(s))

if __name__ == '__main__':
    unittest.main()