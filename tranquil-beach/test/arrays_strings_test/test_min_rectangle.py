import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.min_rectangle import MinRectangle

class TestMinRectangle(unittest.TestCase):
    def setUp(self):
        self.func = MinRectangle().minAreaRect

    def test_1(self):
        points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
        expected = 4
        self.assertEqual(expected, self.func(points))

    def test_2(self):
        points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
        expected = 2
        self.assertEqual(expected, self.func(points))

if __name__ == '__main__':
    unittest.main()