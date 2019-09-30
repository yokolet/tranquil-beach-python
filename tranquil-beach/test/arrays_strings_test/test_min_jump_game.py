import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.min_jump_game import MinJumpGame

class TestMinJumpGame(unittest.TestCase):
    def setUp(self):
        self.func = MinJumpGame().jump

    def test_1(self):
        nums = [2,3,1,1,4]
        expected = 2
        self.assertEqual(expected, self.func(nums))

if __name__ == '__main__':
    unittest.main()