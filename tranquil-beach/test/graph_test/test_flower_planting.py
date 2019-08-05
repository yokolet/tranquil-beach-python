import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.flower_planting import FlowerPlanting

class TestFlowerPlanting(unittest.TestCase):
    def setUp(self):
        self.func = FlowerPlanting().gardenNoAdj

    def test_1(self):
        N, paths = 3, [[1,2],[2,3],[3,1]]
        expected = [[1,3,2],[1,2,3]]
        self.assertTrue(self.func(N, paths) in expected)

    def test_2(self):
        N, paths = 4, [[1,2],[3,4]]
        expected = [[1,2,1,2]]
        self.assertTrue(self.func(N, paths) in expected)

    def test_3(self):
        N, paths = 4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
        expected = [[1,4,2,3],[1,2,3,4]]
        self.assertTrue(self.func(N, paths) in expected)

if __name__ == '__main__':
    unittest.main()