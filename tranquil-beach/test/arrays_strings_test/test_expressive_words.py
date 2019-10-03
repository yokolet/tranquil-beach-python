import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.expressive_words import ExpressiveWords

class TestExpressiveWords(unittest.TestCase):
    def setUp(self):
        self.func = ExpressiveWords().expressiveWords

    def test_1(self):
        S, words = 'heeellooo', ["hello", "hi", "helo"]
        expected = 1
        self.assertEqual(expected, self.func(S, words))

    def test_2(self):
        S = "dddiiiinnssssssoooo"
        words = ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]
        expected = 3
        self.assertEqual(expected, self.func(S, words))

if __name__ == '__main__':
    unittest.main()
