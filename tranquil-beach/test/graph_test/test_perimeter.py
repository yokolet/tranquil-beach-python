import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.perimeter import Perimeter

class TestPerimeter(unittest.TestCase):
    def setUp(self):
        self.func = Perimeter().islandPerimeter

    def test_1(self):
        grid = [
            [0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]
        ]
        expected = 16
        self.assertEqual(expected, self.func(grid))

if __name__ == '__main__':
    unittest.main()