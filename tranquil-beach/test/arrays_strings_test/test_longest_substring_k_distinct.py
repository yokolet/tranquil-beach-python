import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.longest_substring_k_distinct import LongestSubstringKDistinct

class TestLongestSubstringKDistinct(unittest.TestCase):
    def setUp(self):
        self.func = LongestSubstringKDistinct().lengthOfLongestSubstringKDistinct

    def test_1(self):
        s, k = 'eceba', 2
        expected = 3
        self.assertEquals(expected, self.func(s, k))

    def test_2(self):
        s, k = 'aa', 1
        expected = 2
        self.assertEquals(expected, self.func(s, k))

if __name__ == '__main__':
    unittest.main()