import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.num_matrix import NumMatrix

class TestNumMatrix(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
            ]
        func = NumMatrix(matrix)
        self.assertEqual(func.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(func.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(func.sumRegion(1, 2, 2, 4), 12)

    def test_2(self):
        matrix = [[]]
        func = NumMatrix(matrix)
        #self.assertEqual(func.sumRegion(0, 0, 0, 0), 0)

if __name__ == '__main__':
    unittest.main()