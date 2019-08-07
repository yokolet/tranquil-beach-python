import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.tree2str import Tree2Str
from tree.deepest_smallest_subtree import DeepestSmallestSubtree

class TestDeepestSmallestSubtree(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.serializer = Tree2Str()
        self.func = DeepestSmallestSubtree().subtreeWithAllDeepest

    def test_1(self):
        s = "3(5(6)(2(7)(4)))(1(0)(8))"
        expected = "2(7)(4)"
        root = self.builder.str2tree(s)
        self.assertEqual(expected, self.serializer.tree2str(self.func(root)))

if __name__ == '__main__':
    unittest.main()