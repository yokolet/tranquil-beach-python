import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from unittest.mock import Mock, patch
from design.min_stack import MinStack

class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.func = MinStack()

    def test_1(self):
        self.func.push(-2)
        self.func.push(0)
        self.func.push(-3)
        self.assertEqual(self.func.getMin(), -3)
        self.func.pop()
        self.assertEqual(self.func.top(), 0)
        self.assertEqual(self.func.getMin(), -2)

if __name__ == '__main__':
    unittest.main()