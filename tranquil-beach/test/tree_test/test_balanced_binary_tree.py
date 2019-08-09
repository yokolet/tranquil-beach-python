import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.balanced_binary_tree import BalancedBinaryTree

class TestBalancedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = BalancedBinaryTree().isBalanced

    def test_1(self):
        s = "3(9)(20(15)(7))"
        expected = True
        root = self.builder.str2tree(s)
        self.assertTrue(self.func(root))

    def test_2(self):
        s = "1(2(3(4)(4))(3))(2)"
        expected = False
        root = self.builder.str2tree(s)
        self.assertFalse(self.func(root))

if __name__ == '__main__':
    unittest.main()