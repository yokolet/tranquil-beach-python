import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.number_of_islands import NumberOfIslands

class TestNumberOfIslands(unittest.TestCase):
    def setUp(self):
        self.func = NumberOfIslands()

    def test_1(self):
        grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
        expected = 1
        self.assertEqual(self.func.numIslands(grid), expected)

    def test_2(self):
        grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
        expected = 3
        self.assertEqual(self.func.numIslands(grid), expected)

if __name__ == '__main__':
    unittest.main()