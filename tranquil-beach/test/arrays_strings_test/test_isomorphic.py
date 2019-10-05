import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.isomorphic import Isomorphic

class TestIsomorphic(unittest.TestCase):
    def setUp(self):
        self.func = Isomorphic().isIsomorphic

    def test_1(self):
        s, t = 'egg', 'add'
        self.assertTrue(self.func(s, t))

    def test_2(self):
        s, t = 'foo', 'bar'
        self.assertFalse(self.func(s, t))

    def test_3(self):
        s, t = 'paper', 'title'
        self.assertTrue(self.func(s, t))

    def test_4(self):
        s, t = 'aba', 'baa'
        self.assertFalse(self.func(s, t))

    def test_5(self):
        s, t = 'ab', 'aa'
        self.assertFalse(self.func(s, t))

if __name__ == '__main__':
    unittest.main()