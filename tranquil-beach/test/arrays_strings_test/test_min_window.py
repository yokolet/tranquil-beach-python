import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.min_window import MinWindow

class TestMinWindow(unittest.TestCase):
    def setUp(self):
        self.func = MinWindow()

    def test_1(self):
        s, t = "ADOBECODEBANC", "ABC"
        expected = "BANC"
        self.assertEqual(self.func.minWindow(s, t), expected)

if __name__ == '__main__':
    unittest.main()