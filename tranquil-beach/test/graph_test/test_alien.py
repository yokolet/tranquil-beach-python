import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.alien import Alien

class TestAlien(unittest.TestCase):
    def setUp(self):
        self.func = Alien()

    def test_1(self):
        words = [
            "wrt",
            "wrf",
            "er",
            "ett",
            "rftt"
            ]
        expected = "wertf"
        self.assertEqual(self.func.alienOrder(words), expected)

    def test_2(self):
        words = [
            "z",
            "x"
            ]
        expected = "zx"
        self.assertEqual(self.func.alienOrder(words), expected)

    def test_3(self):
        words = [
            "z",
            "x",
            "z"
            ]
        expected = ""
        self.assertEqual(self.func.alienOrder(words), expected)

if __name__ == '__main__':
    unittest.main()