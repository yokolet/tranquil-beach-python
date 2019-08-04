import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.word_search import WordSearch

class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.func = WordSearch().exist
        self.board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
            ]

    def test_1(self):
        word = 'ABCCED'
        expected = True
        self.assertTrue(self.func(self.board, word))
 
    def test_2(self):
        word = 'SEE'
        expected = True
        self.assertTrue(self.func(self.board, word))

    def test_3(self):
        word = 'ABCB'
        expected = False
        self.assertFalse(self.func(self.board, word))

    def test_4(self):
        board4, word = [['a']], 'a'
        self.assertTrue(self.func(board4, word))

    def test_5(self):
        board5, word = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"
        self.assertTrue(self.func(board5, word))

if __name__ == '__main__':
    unittest.main()