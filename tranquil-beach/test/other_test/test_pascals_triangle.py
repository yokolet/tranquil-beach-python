import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.pascals_triangle import PascalsTriangle

class TestPascalsTriangle(unittest.TestCase):
    def setUp(self):
        self.func = PascalsTriangle().generate

    def test_1(self):
        n = 5
        expected = [
            [1],
            [1,1],
            [1,2,1],
            [1,3,3,1],
            [1,4,6,4,1]
        ]
        self.assertEqual(expected, self.func(n))

if __name__ == '__main__':
    unittest.main()