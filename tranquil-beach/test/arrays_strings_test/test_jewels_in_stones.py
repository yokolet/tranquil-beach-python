import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.jewels_in_stones import JewelsInStones

class TestJewelsInStones(unittest.TestCase):
    def setUp(self):
        self.func = JewelsInStones().numJewelsInStones

    def test_1(self):
        J, S = 'aA', 'aAAbbbb'
        expected = 3
        self.assertEquals(expected, self.func(J, S))

    def test_2(self):
        J, S = 'z', 'ZZ'
        expected = 0
        self.assertEquals(expected, self.func(J, S))

if __name__ == '__main__':
    unittest.main()