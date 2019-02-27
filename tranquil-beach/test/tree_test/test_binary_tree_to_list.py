import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.tree2str import Tree2Str
from tree.binary_tree_to_list import BinaryTreeToList

class TestBinaryTreeToList(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.serializer = Tree2Str()
        self.func = BinaryTreeToList()

    def test_1(self):
        s = "1(2(3)(4))(5()(6))"
        expected = "1()(2()(3()(4()(5()(6)))))"
        root = self.builder.str2tree(s)
        self.func.flatten(root)
        self.assertEqual(self.serializer.tree2str(root), expected)


if __name__ == '__main__':
    unittest.main()