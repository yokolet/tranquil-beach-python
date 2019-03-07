import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.closest_value import ClosestValue

class TestClosestValue(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = ClosestValue()

    def test_1(self):
        s, target = "4(2(1)(3))(5)", 3.714286
        expected = 4
        root = self.builder.str2tree(s)
        self.assertEqual(self.func.closestValue(root, target), expected)

if __name__ == '__main__':
    unittest.main()