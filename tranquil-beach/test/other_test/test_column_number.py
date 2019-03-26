import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.column_number import ColumnNumber

class TestColumnNumber(unittest.TestCase):
    def setUp(self):
        self.func = ColumnNumber()

    def test_1(self):
        s = "A"
        expected = 1
        self.assertEqual(self.func.titleToNumber(s), expected)

    def test_2(self):
        s = "AB"
        expected = 28
        self.assertEqual(self.func.titleToNumber(s), expected)

    def test_3(self):
        s = "ZY"
        expected = 701
        self.assertEqual(self.func.titleToNumber(s), expected)

if __name__ == '__main__':
    unittest.main()