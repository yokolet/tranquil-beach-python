import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.unique_paths_obstacles import UniquePathsObstacles

class TestUniquePathsObstacles(unittest.TestCase):
    def setUp(self):
        self.func = UniquePathsObstacles().uniquePathsWithObstacles

    def test_1(self):
        grid = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        expected = 2
        self.assertEquals(expected, self.func(grid))

    def test_2(self):
        grid = [
            [1]
        ]
        expected = 0
        self.assertEquals(expected, self.func(grid))

    def test_3(self):
        grid = [
            [0]
        ]
        expected = 1
        self.assertEquals(expected, self.func(grid))

    def test_4(self):
        grid = [
            [1, 0]
        ]
        expected = 0
        self.assertEquals(expected, self.func(grid))

if __name__ == '__main__':
    unittest.main()