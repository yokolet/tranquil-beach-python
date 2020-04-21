import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.leftmost_column import BinaryMatrix, LeftmostColumn

class TestLicenseKey(unittest.TestCase):
    def setUp(self):
        self.func = LeftmostColumn().leftMostColumnWithOne

    def test_1(self):
        mat = [[1,1,1,1,1],[0,0,0,1,1],[0,0,1,1,1],[0,0,0,0,1],[0,0,0,0,0]]
        bm = BinaryMatrix(mat)
        expected = 0
        self.assertEqual(expected, self.func(bm))

    def test_2(self):
        mat = [[0,0],[1,1]]
        bm = BinaryMatrix(mat)
        expected = 0
        self.assertEqual(expected, self.func(bm))

    def test_3(self):
        mat = [[0,0],[0,1]]
        bm = BinaryMatrix(mat)
        expected = 1
        self.assertEqual(expected, self.func(bm))
    
    def test_4(self):
        mat = [[0,0],[0,0]]
        bm = BinaryMatrix(mat)
        expected = -1
        self.assertEqual(expected, self.func(bm))

    def test_5(self):
        mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
        bm = BinaryMatrix(mat)
        expected = 1
        self.assertEqual(expected, self.func(bm))

    def test_6(self):
        # too many calls error -- fixed
        from test_leftmost_column_data import mat0, mat1
        bm = BinaryMatrix(mat0)
        expected = 39
        self.assertEqual(expected, self.func(bm))

    def test_7(self):
        # too many calls error -- fixed
        from test_leftmost_column_data import mat0, mat1
        bm = BinaryMatrix(mat1)
        expected = 38
        self.assertEqual(expected, self.func(bm))

if __name__ == '__main__':
    unittest.main()
