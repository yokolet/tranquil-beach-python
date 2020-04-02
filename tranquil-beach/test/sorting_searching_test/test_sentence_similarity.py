import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.sentence_similarity import SentenceSimilarity

class TestSentenceSimilarity(unittest.TestCase):
    def setUp(self):
        self.func = SentenceSimilarity().areSentencesSimilar

    def test_1(self):
        pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]
        words1, words2 = ['great', 'acting', 'skills'], ['fine', 'drama', 'talent']
        self.assertTrue(self.func(words1, words2, pairs))

    def test_2(self):
        pairs = []
        words1, words2 = ['great'], ['great']
        self.assertTrue(self.func(words1, words2, pairs))

    def test_3(self):
        pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]
        words1, words2 = ['great'], ['great', 'fine']
        self.assertFalse(self.func(words1, words2, pairs))

    def test_4(self):
        words1 = ["an","extraordinary","meal"]
        words2 = ["one","good","dinner"]
        pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],
                ["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],
                ["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],
                ["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],
                ["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],
                ["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],
                ["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],
                ["really","very"],["super","very"]]
        self.assertTrue(self.func(words1, words2, pairs))

if __name__ == '__main__':
    unittest.main()