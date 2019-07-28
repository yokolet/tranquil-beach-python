import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.snakes_ladders import SnakesLadders

class TestSnakesLadders(unittest.TestCase):
    def setUp(self):
        self.func = SnakesLadders().snakesAndLadders

    def test_1(self):
        board = [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,35,-1,-1,13,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,15,-1,-1,-1,-1]
        ]
        expected = 4
        self.assertEquals(expected, self.func(board))

if __name__ == '__main__':
    unittest.main()