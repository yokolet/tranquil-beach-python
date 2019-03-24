import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.valid_number import ValidNumber

class TestValidNumber(unittest.TestCase):
    def setUp(self):
        self.func = ValidNumber()

    def test_1(self):
        s = "0"
        self.assertTrue(self.func.isNumber(s))

    def test_2(self):
        s = " 0.1 "
        self.assertTrue(self.func.isNumber(s))

    def test_3(self):
        s = "abc"
        self.assertFalse(self.func.isNumber(s))

    def test_4(self):
        s = "1 a"
        self.assertFalse(self.func.isNumber(s))

    def test_5(self):
        s = "2e10"
        self.assertTrue(self.func.isNumber(s))

    def test_6(self):
        s = " -90e3   "
        self.assertTrue(self.func.isNumber(s))

    def test_7(self):
        s = " 1e"
        self.assertFalse(self.func.isNumber(s))

    def test_8(self):
        s = "e3"
        self.assertFalse(self.func.isNumber(s))

    def test_9(self):
        s = " 6e-1"
        self.assertTrue(self.func.isNumber(s))

    def test_10(self):
        s = " 99e2.5 "
        self.assertFalse(self.func.isNumber(s))

    def test_11(self):
        s = "53.5e93"
        self.assertTrue(self.func.isNumber(s))

    def test_12(self):
        s = " --6 "
        self.assertFalse(self.func.isNumber(s))

    def test_13(self):
        s = "-+3"
        self.assertFalse(self.func.isNumber(s))

    def test_14(self):
        s = "95a54e53"
        self.assertFalse(self.func.isNumber(s))

    def test_15(self):
        s = ".1"
        self.assertTrue(self.func.isNumber(s))

    def test_156(self):
        s = "3."
        self.assertTrue(self.func.isNumber(s))

if __name__ == '__main__':
    unittest.main()