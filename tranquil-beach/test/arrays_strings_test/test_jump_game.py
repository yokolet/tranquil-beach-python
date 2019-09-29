import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.jump_game import JumpGame

class TestJumpGame(unittest.TestCase):
    def setUp(self):
        self.func = JumpGame().canJump

    def test_1(self):
        nums = [2,3,1,1,4]
        self.assertTrue(self.func(nums))

    def test_2(self):
        nums = [3,2,1,0,4]
        self.assertFalse(self.func(nums))

if __name__ == '__main__':
    unittest.main()