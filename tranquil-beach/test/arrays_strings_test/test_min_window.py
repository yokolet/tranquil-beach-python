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

    def test_2(self):
        s, t = 'ab', 'b'
        expected = 'b'
        self.assertEqual(self.func.minWindow(s, t), expected)

    def test_3(self):
        s, t = "a", "aa"
        expected = ''
        self.assertEqual(self.func.minWindow(s, t), expected)

    def test_4(self):
        s, t = "a", "b"
        expected = ''
        self.assertEqual(self.func.minWindow(s, t), expected)

    def test_5(self):
        s, t = "acbbaca", "aba"
        expected = "baca"
        self.assertEqual(self.func.minWindow(s, t), expected)

if __name__ == '__main__':
    unittest.main()