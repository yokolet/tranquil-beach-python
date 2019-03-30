import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.func = Maze()

    def test_1(self):
        maze = [
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]
        ]
        start, destination = [0,4],[4,4]
        self.assertTrue(self.func.hasPath(maze, start, destination))

    def test_2(self):
        maze = [
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]
        ]
        start, destination = [0,4],[3,2]
        self.assertFalse(self.func.hasPath(maze, start, destination))

if __name__ == '__main__':
    unittest.main()