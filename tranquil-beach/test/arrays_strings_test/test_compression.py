import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.compression import Compression

class TestCompression(unittest.TestCase):
    def setUp(self):
        self.func = Compression().countAndSay

    def test_1(self):
        n = 1
        expected = "1"
        self.assertEqual(expected, self.func(n))

    def test_2(self):
        n = 4
        expected = "1211"
        self.assertEqual(expected, self.func(n))

if __name__ == '__main__':
    unittest.main()