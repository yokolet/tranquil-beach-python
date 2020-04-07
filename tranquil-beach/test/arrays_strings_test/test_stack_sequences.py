import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.stack_sequences import StackSequences

class TestStackSequences(unittest.TestCase):
    def setUp(self):
        self.func = StackSequences().validateStackSequences

    def test_1(self):
        pushed, popped = [1,2,3,4,5], [4,5,3,2,1]
        self.assertTrue(self.func(pushed, popped))

    def test_2(self):
        pushed, popped = [1,2,3,4,5], [4,3,5,1,2]
        self.assertFalse(self.func(pushed, popped))

if __name__ == '__main__':
    unittest.main()
