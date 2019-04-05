import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.ladder_length import LadderLength

class TestLadderLength(unittest.TestCase):
    def setUp(self):
        self.func = LadderLength()

    def test_1(self):
        beginWord, endWord = "hit", "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        expected = 5
        self.assertEqual(self.func.ladderLength(beginWord, endWord, wordList), expected)

    def test_2(self):
        beginWord, endWord = "hit", "cog"
        wordList = ["hot","dot","dog","lot","log"]
        expected = 0
        self.assertEqual(self.func.ladderLength(beginWord, endWord, wordList), expected)

if __name__ == '__main__':
    unittest.main()