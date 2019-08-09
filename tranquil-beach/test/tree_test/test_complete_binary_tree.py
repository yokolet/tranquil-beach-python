import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.complete_binary_tree import CompleteBinaryTree

class TestCompleteBinaryTree(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = CompleteBinaryTree().isCompleteTree

    def test_1(self):
        s = "1(2(4)(5))(3(6))"
        expected = True
        root = self.builder.str2tree(s)
        self.assertTrue(self.func(root))

    def test_2(self):
        s = "1(2(4)(5))(3()(7))"
        expected = False
        root = self.builder.str2tree(s)
        self.assertFalse(self.func(root))

if __name__ == '__main__':
    unittest.main()