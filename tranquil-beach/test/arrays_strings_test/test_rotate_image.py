import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.rotate_image import RotateImage

class TestRotateImage(unittest.TestCase):
    def setUp(self):
        self.func = RotateImage().rotate

    def test_1(self):
        m = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ]
        expected = [
            [7,4,1],
            [8,5,2],
            [9,6,3]
            ]
        self.func(m)
        self.assertEqual(expected, m)

    def test_2(self):
        m = [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
            ]
        expected = [
            [15,13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7,10,11]
            ]
        self.func(m)
        self.assertEqual(expected, m)

    def test_3(self):
        m = [
            [ 1, 2, 3, 4, 5],
            [ 6, 7, 8, 9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]
            ]
        expected = [
            [21,16,11, 6, 1],
            [22,17,12, 7, 2],
            [23,18,13, 8, 3],
            [24,19,14, 9, 4],
            [25,20,15,10, 5]
            ]
        self.func(m)
        self.assertEqual(expected, m)

if __name__ == '__main__':
    unittest.main()