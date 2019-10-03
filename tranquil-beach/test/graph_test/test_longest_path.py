import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.longest_path import LongestPath

class TestLongestPath(unittest.TestCase):
    def setUp(self):
        self.func = LongestPath().longestIncreasingPath

    def test_1(self):
        matrix = [
                    [9,9,4],
                    [6,6,8],
                    [2,1,1]
                ]
        expected = 4
        self.assertEqual(expected, self.func(matrix))
    
    def test_2(self):
        matrix = [
                    [3,4,5],
                    [3,2,6],
                    [2,2,1]
                ]
        expected = 4
        self.assertEqual(expected, self.func(matrix))

    def test_3(self):
        matrix = [[1]]
        expected = 1
        self.assertEqual(expected, self.func(matrix))

if __name__ == '__main__':
    unittest.main()