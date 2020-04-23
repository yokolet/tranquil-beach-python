import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.bitwise_and import BitwiseAnd

class TestCatalanNumber(unittest.TestCase):
    def setUp(self):
        self.func = BitwiseAnd().rangeBitwiseAnd

    def test_1(self):
        m, n = 5, 7
        expected = 4
        self.assertEqual(expected, self.func(m, n))

    def test_2(self):
        m, n = 0, 1
        expected = 0
        self.assertEqual(expected, self.func(m, n))

    def test_3(self):
        m, n = 1, 2
        expected = 0
        self.assertEqual(expected, self.func(m, n))

    def test_4(self):
        m, n = 5, 6
        expected = 4
        self.assertEqual(expected, self.func(m, n))

if __name__ == '__main__':
    unittest.main()
