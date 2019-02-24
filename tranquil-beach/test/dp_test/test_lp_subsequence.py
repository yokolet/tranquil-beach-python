import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.lp_subsequence import LongestPalindromicSubsequence

class TestLongestPalindromicSubsequence(unittest.TestCase):
    def setUp(self):
        self.func = LongestPalindromicSubsequence()

    def test_1(self):
        s = "bbbab"
        expected = 4
        self.assertEqual(self.func.longestPalindromeSubseq(s), expected)

    def test_2(self):
        s = "cbbd"
        expected = 2
        self.assertEqual(self.func.longestPalindromeSubseq(s), expected)

if __name__ == '__main__':
    unittest.main()