import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.min_path import MinPath

class TestMinPath(unittest.TestCase):
    def setUp(self):
        self.func = MinPath().minPathSum

    def test_1(self):
        grid = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
        ]
        expected = 7
        self.assertEqual(expected, self.func(grid))

if __name__ == '__main__':
    unittest.main()
