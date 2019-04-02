import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.flood_fill import FloodFill

class TestFloodFill(unittest.TestCase):
    def setUp(self):
        self.func = FloodFill()

    def test_1(self):
        image = [
            [1,1,1],
            [1,1,0],
            [1,0,1]
            ]
        sr, sc, newColor = 1, 1, 2
        expected = [
            [2,2,2],
            [2,2,0],
            [2,0,1]
            ]
        self.assertEqual(self.func.floodFill(image, sr, sc, newColor), expected)

    def test_2(self):
        image = [[0,0,0],[0,0,0]]
        sr, sc, newColor = 0, 0, 2
        expected = [[2,2,2],[2,2,2]]
        self.assertEqual(self.func.floodFill(image, sr, sc, newColor), expected)

    def test_3(self):
        image = [[0,0,0],[0,1,1]]
        sr, sc, newColor = 1, 1, 1
        expected = [[0,0,0],[0,1,1]]
        self.assertEqual(self.func.floodFill(image, sr, sc, newColor), expected)

if __name__ == '__main__':
    unittest.main()