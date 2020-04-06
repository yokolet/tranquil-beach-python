import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.hand_of_straights import HandOfStraights

class TestHandOfStraights(unittest.TestCase):
    def setUp(self):
        self.func = HandOfStraights().isNStraightHand

    def test_1(self):
        hand, W = [1,2,3,6,2,3,4,7,8], 3
        self.assertTrue(self.func(hand, W))

    def test_2(self):
        hand, W = [1,2,3,4,5], 4
        self.assertFalse(self.func(hand, W))

    def test_3(self):
        hand, W = [2,4,6], 3
        self.assertFalse(self.func(hand, W))

if __name__ == '__main__':
    unittest.main()
