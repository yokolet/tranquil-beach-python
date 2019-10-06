import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.valid_square import ValidSquare

class TestValidSquare(unittest.TestCase):
    def setUp(self):
        self.func = ValidSquare().validSquare

    def test_1(self):
        p1, p2, p3, p4 = [0,0], [1,1], [1,0], [0,1]
        self.assertTrue(self.func(p1, p2, p3, p4))

    def test_2(self):
        p1, p2, p3, p4 = [0,0], [0,0], [0,0], [0,0]
        self.assertFalse(self.func(p1, p2, p3, p4))

if __name__ == '__main__':
    unittest.main()