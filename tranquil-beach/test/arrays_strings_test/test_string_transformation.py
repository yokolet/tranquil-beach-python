import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.string_transformation import StringTransformation

class TestStringTransformation(unittest.TestCase):
    def setUp(self):
        self.func = StringTransformation().canConvert

    def test_1(self):
        str1, str2 = 'aabcc', 'ccdee'
        self.assertTrue(self.func(str1, str2))

    def test_2(self):
        str1, str2 = 'leetcode', 'codeleet'
        self.assertFalse(self.func(str1, str2))

    def test_3(self):
        str1, str2 = 'abcdefghijklmnopqrstuvwxyz', 'bcdefghijklmnopqrstuvwxyza'
        self.assertFalse(self.func(str1, str2))

    def test_4(self):
        str1, str2 = 'abcdefghijklmnopqrstuvwxyz', 'bcdefghijklmnopqrstuvwxyzq'
        self.assertTrue(self.func(str1, str2))

if __name__ == '__main__':
    unittest.main()
