import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.column_title import ColumnTitle

class TestColumnTitle(unittest.TestCase):
    def setUp(self):
        self.func = ColumnTitle()

    def test_1(self):
        n = 1
        expected = "A"
        self.assertEqual(self.func.convertToTitle(n), expected)

    def test_2(self):
        n = 28
        expected = "AB"
        self.assertEqual(self.func.convertToTitle(n), expected)

    def test_3(self):
        n = 701
        expected = "ZY"
        self.assertEqual(self.func.convertToTitle(n), expected)


if __name__ == '__main__':
    unittest.main()