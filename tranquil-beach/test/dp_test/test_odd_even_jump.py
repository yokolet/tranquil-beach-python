import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.odd_even_jump import OddEvenJump

class TestOddEvenJump(unittest.TestCase):
    def setUp(self):
        self.func = OddEvenJump().oddEvenJumps

    def test_1(self):
        a = [10,13,12,14,15]
        expected = 2
        self.assertEqual(expected, self.func(a))

    def test_2(self):
        a = [2,3,1,1,4]
        expected = 3
        self.assertEqual(expected, self.func(a))

    def test_3(self):
        a = [5,1,3,4,2]
        expected = 3
        self.assertEqual(expected, self.func(a))

if __name__ == '__main__':
    unittest.main()