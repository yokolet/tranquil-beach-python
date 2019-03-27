import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.top_words import TopWords

class TestTopWords(unittest.TestCase):
    def setUp(self):
        self.func = TopWords()

    def test_1(self):
        words, k = ["i", "love", "leetcode", "i", "love", "coding"], 2
        expected = ["i", "love"]
        self.assertEqual(self.func.topKFrequent(words, k), expected)

    def test_2(self):
        words, k = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
        expected = ["the", "is", "sunny", "day"]
        self.assertEqual(self.func.topKFrequent(words, k), expected)

if __name__ == '__main__':
    unittest.main()