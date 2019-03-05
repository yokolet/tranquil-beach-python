import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.longest_substring import LongestSubstring

class TestLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.func = LongestSubstring()

    def test_1(self):
        s = "abcabcbb"
        expected = 3 
        self.assertEqual(self.func.lengthOfLongestSubstring(s), expected)

    def test_2(self):
        s = "bbbbb"
        expected = 1
        self.assertEqual(self.func.lengthOfLongestSubstring(s), expected)

    def test_3(self):
        s = "pwwkew"
        expected = 3
        self.assertEqual(self.func.lengthOfLongestSubstring(s), expected)

    def test_4(self):
        s = " "
        expected = 1
        self.assertEqual(self.func.lengthOfLongestSubstring(s), expected)

    def test_5(self):
        s = "au"
        expected = 2
        self.assertEqual(self.func.lengthOfLongestSubstring(s), expected)

    def test_6(self):
        s = "dvdf"
        expected = 3
        self.assertEqual(self.func.lengthOfLongestSubstring(s), expected)

if __name__ == '__main__':
    unittest.main()