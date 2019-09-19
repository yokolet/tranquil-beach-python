import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.domino_rotations import DominoRotations

class TestDominoRotations(unittest.TestCase):
    def setUp(self):
        self.func = DominoRotations().minDominoRotations

    def test_1(self):
        A, B = [2,1,2,4,2,2], [5,2,6,2,3,2]
        expected = 2
        self.assertEqual(expected, self.func(A, B))

    def test_2(self):
        A, B = [3,5,1,2,3], [3,6,3,3,4]
        expected = -1
        self.assertEqual(expected, self.func(A, B))

if __name__ == '__main__':
    unittest.main()