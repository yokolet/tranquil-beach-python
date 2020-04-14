import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.tree2str import Tree2Str
from tree.flipped_binary_tree import FlippedBinaryTree

class TestFlippedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree().str2tree
        self.serializer = Tree2Str().tree2str
        self.func = FlippedBinaryTree().flipEquiv

    def test_1(self):
        s1, s2 = "1(2(4)(5(7)(8)))(3(6))", "1(3()(6))(2(4)(5(8)(7)))"
        expected = True
        root1, root2 = self.builder(s1), self.builder(s2)
        self.assertTrue(self.func(root1, root2))

if __name__ == '__main__':
    unittest.main()
