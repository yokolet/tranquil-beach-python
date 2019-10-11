import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.spiral_matrix import SpiralMatrix

class TestSpiralMatrix(unittest.TestCase):
    def setUp(self):
        self.func = SpiralMatrix().spiralOrder

    def test_1(self):
        matrix = [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(expected, self.func(matrix))

    def test_2(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12]
        ]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(expected, self.func(matrix))

if __name__ == '__main__':
    unittest.main()