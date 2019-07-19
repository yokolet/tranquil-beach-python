import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.unique_paths_obstacles_ham import UniquePathsObstaclesHam

class TestUniquePathsObstaclesHam(unittest.TestCase):
    def setUp(self):
        self.func = UniquePathsObstaclesHam().uniquePathsIII

    def test_1(self):
        grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
        expected = 2
        self.assertAlmostEquals(expected, self.func(grid))

    def test_2(self):
        grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
        expected = 4
        self.assertAlmostEquals(expected, self.func(grid))

    def test_3(self):
        grid = [[0,1],[2,0]]
        expected = 0
        self.assertAlmostEquals(expected, self.func(grid))

if __name__ == '__main__':
    unittest.main()