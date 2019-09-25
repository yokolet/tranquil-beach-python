import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.form_string import FormString

class TestFormString(unittest.TestCase):
    def setUp(self):
        self.func = FormString().shortestWay

    def test_1(self):
        s, t = 'abc', 'abcbc'
        expected = 2
        self.assertEqual(expected, self.func(s, t))

    def test_2(self):
        s, t = 'abc', 'abcdbc'
        expected = -1
        self.assertEqual(expected, self.func(s, t))

    def test_3(self):
        s, t = 'xyz', 'xzyxz'
        expected = 3
        self.assertEqual(expected, self.func(s, t))

    def test_4(self):
        s, t = 'aaaaa', 'aaaaaaaaaaaaa'
        expected = 3
        self.assertEqual(expected, self.func(s, t))

if __name__ == '__main__':
    unittest.main()