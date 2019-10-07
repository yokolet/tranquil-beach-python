import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.word_break import WordBreak

class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.func = WordBreak().wordBreak

    def test_1(self):
        s, wordDict = 'leetcode', ["leet", "code"]
        self.assertTrue(self.func(s, wordDict))

    def test_2(self):
        s, wordDict = 'applepenapple', ["apple", "pen"]
        self.assertTrue(self.func(s, wordDict))

    def test_3(self):
        s, wordDict = 'catsandog', ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.func(s, wordDict))

if __name__ == '__main__':
    unittest.main()