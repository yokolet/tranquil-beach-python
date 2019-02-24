import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.lp_substring import LongestPalindromicSubstring

class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self):
        self.func = LongestPalindromicSubstring()

    def test_1(self):
        s = "babad"
        expected1 = "bab"
        expected2 = "aba"
        self.assertIn(self.func.longestPalindrome(s), [expected1, expected2])

if __name__ == '__main__':
    unittest.main()
