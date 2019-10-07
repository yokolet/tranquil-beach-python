import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.max_square import MaxSquare

class TestMaxSquare(unittest.TestCase):
    def setUp(self):
        self.func = MaxSquare().maximalSquare

    def test_1(self):
        matrix = [
            ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '1', '0'],
        ]
        expected = 4
        self.assertEqual(expected, self.func(matrix))

if __name__ == '__main__':
    unittest.main()