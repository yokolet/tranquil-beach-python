import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.backspace import Backspace

class TestBackspace(unittest.TestCase):
    def setUp(self):
        self.func = Backspace().backspaceCompare

    def test_1(self):
        s, t = 'ab#c', 'ad#c'
        self.assertTrue(self.func(s, t))

    def test_2(self):
        s, t = 'ab##', 'c#d#'
        self.assertTrue(self.func(s, t))

    def test_3(self):
        s, t = 'a##c', '#a#c'
        self.assertTrue(self.func(s, t))

    def test_4(self):
        s, t = 'a#c', 'b'
        self.assertFalse(self.func(s, t))

    def test_5(self):
        s, t = 'y#fo##f', 'y#f#o##f'
        self.assertTrue(self.func(s, t))

if __name__ == '__main__':
    unittest.main()