import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.stone_removing import StoneRemoving

class TestStoneRemoving(unittest.TestCase):
    def setUp(self):
        self.func = StoneRemoving().removeStones

    def test_1(self):
        stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
        expected = 5
        self.assertEqual(expected, self.func(stones))

    def test_2(self):
        stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
        expected = 3
        self.assertEqual(expected, self.func(stones))

    def test_3(self):
        stones = [[0,0]]
        expected = 0
        self.assertEqual(expected, self.func(stones))

if __name__ == '__main__':
    unittest.main()