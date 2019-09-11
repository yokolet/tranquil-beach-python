import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.campus_bikes import CampusBikes

class TestCampusBikes(unittest.TestCase):
    def setUp(self):
        self.func = CampusBikes().assignBikes

    def test_1(self):
        workers = [[0,0],[2,1]]
        bikes = [[1,2],[3,3]]
        expected = [1,0]
        self.assertEqual(expected, self.func(workers, bikes))

    def test_2(self):
        workers = [[0,0],[1,1],[2,0]]
        bikes = [[1,0],[2,2],[2,1]]
        expected = [0,2,1]
        self.assertEqual(expected, self.func(workers, bikes))

if __name__ == '__main__':
    unittest.main()