import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.matrix import Matrix

class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.func = Matrix().searchMatrix

    def test_1(self):
        matrix, target = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 3
        self.assertTrue(self.func(matrix, target))

    def test_2(self):
        matrix, target = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 13
        self.assertFalse(self.func(matrix, target))

    def test_3(self):
        matrix, target = [
            [1,  3, 5, 7],
            [10,11,16,20],
            [23,30,34,50]
        ], 10
        self.assertTrue(self.func(matrix, target))

if __name__ == '__main__':
    unittest.main()