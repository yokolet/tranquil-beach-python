import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.catalan_number import CatalanNumber

class TestCatalanNumber(unittest.TestCase):
    def setUp(self):
        self.func = CatalanNumber().numTrees2
    def test_1(self):
        n = 3
        expected = 5
        self.assertEqual(expected, self.func(n))

    def test_2(self):
        n = 7
        expected = 429
        self.assertEqual(expected, self.func(n))

if __name__ == '__main__':
    unittest.main()