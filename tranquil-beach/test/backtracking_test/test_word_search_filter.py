import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.word_search_filter import WordSearchFilter

class TestWordSearchFilter(unittest.TestCase):
    def setUp(self):
        self.func = WordSearchFilter().findWords

    def test_1(self):
        board = [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
            ]
        words = ["oath","pea","eat","rain"]
        expected = ["eat","oath"]
        self.assertCountEqual(expected, self.func(board, words))

if __name__ == '__main__':
    unittest.main()