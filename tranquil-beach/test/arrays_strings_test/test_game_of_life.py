import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.game_of_life import GameOfLife

class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        self.func = GameOfLife()

    def test_1(self):
        board = [
            [0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]
            ]
        expected = [
            [0,0,0],
            [1,0,1],
            [0,1,1],
            [0,1,0]
            ]
        self.func.gameOfLife(board)
        self.assertEqual(board, expected)

if __name__ == '__main__':
    unittest.main()