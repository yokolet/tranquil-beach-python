import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.word_squares import WordSquares

class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.func = WordSquares().wordSquares

    def test_1(self):
        words = ["area","lead","wall","lady","ball"]
        expected = [[
            "wall",
            "area",
            "lead",
            "lady"
            ],[
            "ball",
            "area",
            "lead",
            "lady"
            ]]
        self.assertCountEqual(expected, self.func(words))

    def test_2(self):
        words = ["abat","baba","atan","atal"]
        expected = [[
            "baba",
            "abat",
            "baba",
            "atan"
            ],[
            "baba",
            "abat",
            "baba",
            "atal"
            ]]
        self.assertCountEqual(expected, self.func(words))

if __name__ == '__main__':
    unittest.main()
