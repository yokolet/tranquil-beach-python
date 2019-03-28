import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.shortest_distance import ShortestDistance

class TestShortestDistance(unittest.TestCase):
    def setUp(self):
        self.func = ShortestDistance()

    def test_1(self):
        grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
        expected = 7
        self.assertEqual(self.func.shortestDistance(grid), expected)

if __name__ == '__main__':
    unittest.main()