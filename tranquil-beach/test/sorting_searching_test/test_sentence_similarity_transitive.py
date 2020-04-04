import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.sentence_similarity_transitive import SentenceSimilarityTransitive

class TestSentenceSimilarityTransitive(unittest.TestCase):
    def setUp(self):
        self.func = SentenceSimilarityTransitive().areSentencesSimilarTwo

    def test_1(self):
        pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]
        words1, words2 = ['great', 'acting', 'skills'], ['fine', 'drama', 'talent']
        self.assertTrue(self.func(words1, words2, pairs))

    def test_2(self):
        from test_sentence_similarity_transitive_data import words1, words2, pairs
        self.assertTrue(self.func(words1, words2, pairs))
    
    def test_3(self):
        words1 = ["an","extraordinary","meal","meal"]
        words2 = ["one","good","dinner"]
        pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],
                ["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],
                ["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],
                ["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],
                ["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
        self.assertFalse(self.func(words1, words2, pairs))

if __name__ == '__main__':
    unittest.main()