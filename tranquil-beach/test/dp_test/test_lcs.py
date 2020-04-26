import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.lcs import LCS

class TestLCS(unittest.TestCase):
    def setUp(self):
        self.func = LCS().longestCommonSubsequence

    def test_1(self):
        text1, text2 = "abcde", "ace" 
        expected = 3
        self.assertEqual(expected, self.func(text1, text2))

    def test_2(self):
        text1, text2 = "abc", "abc"
        expected = 3
        self.assertEqual(expected, self.func(text1, text2))

    def test_3(self):
        text1, text2 = "abc", "def"
        expected = 0
        self.assertEqual(expected, self.func(text1, text2))

    def test_4(self):
        text1, text2 = 'abcdef', 'acbcf'
        expected = 4
        self.assertEqual(expected, self.func(text1, text2))

if __name__ == '__main__':
    unittest.main()
