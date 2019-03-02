import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.sqrt_approx import SqrtApprox

class TestSqrtApprox(unittest.TestCase):
    def setUp(self):
        self.func = SqrtApprox()

    def test_1(self):
        x =  4
        expected = 2
        self.assertEqual(self.func.mySqrt(x), expected)

    def test_2(self):
        x =  8
        expected = 2
        self.assertEqual(self.func.mySqrt(x), expected)

if __name__ == '__main__':
    unittest.main()