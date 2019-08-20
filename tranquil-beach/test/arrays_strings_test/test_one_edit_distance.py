import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.one_edit_distance import OneEditDistance

class TestOneEditDistance(unittest.TestCase):
    def setUp(self):
        self.func = OneEditDistance().isOneEditDistance

    def test_1(self):
        s, t = 'ab', 'acb'
        self.assertTrue(self.func(s, t))

    def test_2(self):
        s, t = 'cab', 'ad'
        self.assertFalse(self.func(s, t))

    def test_3(self):
        s, t = '1203', '1213'
        self.assertTrue(self.func(s, t))

    def test_4(self):
        s, t = '', ''
        self.assertFalse(self.func(s, t))

    def test_5(self):
        s, t = 'a', ''
        self.assertTrue(self.func(s, t))

    def test_6(self):
        s, t = 'c', 'c'
        self.assertFalse(self.func(s, t))

if __name__ == '__main__':
    unittest.main()