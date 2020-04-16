import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.valid_string import ValidString

class TestWildcard(unittest.TestCase):
    def setUp(self):
        self.func = ValidString().checkValidString

    def test_1(self):
        s = '()'
        self.assertTrue(self.func(s))

    def test_2(self):
        s = '(*)'
        self.assertTrue(self.func(s))

    def test_3(self):
        s = '(*))'
        self.assertTrue(self.func(s))

    def test_4(self):
        s = '*'
        self.assertTrue(self.func(s))

    def test_5(self):
        s = '(())((())()()(*)(*()(())())())()()((()())((()))(*'
        self.assertFalse(self.func(s))

if __name__ == '__main__':
    unittest.main()
