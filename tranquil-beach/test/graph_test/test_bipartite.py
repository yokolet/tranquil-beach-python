import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.bipartite import Bipartite

class TestBipartite(unittest.TestCase):
    def setUp(self):
        self.func = Bipartite()

    def test_1(self):
        graph = [[1,3], [0,2], [1,3], [0,2]]
        self.assertTrue(self.func.isBipartite(graph))

    def test_2(self):
        graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
        self.assertFalse(self.func.isBipartite(graph))

if __name__ == '__main__':
    unittest.main()