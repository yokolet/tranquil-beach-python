import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.fruit_baskets import FruitBaskets

class TestFruitBaskets(unittest.TestCase):
    def setUp(self):
        self.func = FruitBaskets().totalFruit

    def test_1(self):
        tree = [1,2,1]
        expected = 3
        self.assertEqual(expected, self.func(tree))

    def test_2(self):
        tree = [0,1,2,2]
        expected = 3
        self.assertEqual(expected, self.func(tree))

    def test_3(self):
        tree = [1,2,3,2,2]
        expected = 4
        self.assertEqual(expected, self.func(tree))

    def test_4(self):
        tree = [3,3,3,1,2,1,1,2,3,3,4]
        expected = 5
        self.assertEqual(expected, self.func(tree))

if __name__ == '__main__':
    unittest.main()