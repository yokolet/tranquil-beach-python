import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.hamming_distance import HammingDistance

class TestFraction(unittest.TestCase):
    def setUp(self):
        self.func = HammingDistance().hammingDistance

    def test_1(self):
        x, y = 1, 4
        expected = 2
        self.assertEqual(expected, self.func(x, y))

if __name__ == '__main__':
    unittest.main()
