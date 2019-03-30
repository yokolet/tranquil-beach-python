import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.prison_cells import PrisonCells

class TestPrisonCells(unittest.TestCase):
    def setUp(self):
        self.func = PrisonCells()

    def test_1(self):
        cells, N = [0,1,0,1,1,0,0,1], 7
        expected = [0,0,1,1,0,0,0,0]
        self.assertEqual(self.func.prisonAfterNDays(cells, N), expected)

    def test_2(self):
        cells, N = [1,0,0,1,0,0,1,0], 1000000000
        expected = [0,0,1,1,1,1,1,0]
        self.assertEqual(self.func.prisonAfterNDays(cells, N), expected)


if __name__ == '__main__':
    unittest.main()