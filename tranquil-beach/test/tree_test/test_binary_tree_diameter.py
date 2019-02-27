import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.binary_tree_diameter import BinaryTreeDiameter

class TestBinaryTreeDiameter(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = BinaryTreeDiameter()

    def test_1(self):
        s = "1(2(4)(5))(3)"
        expected = 3
        root = self.builder.str2tree(s)
        result = self.func.diameterOfBinaryTree(root)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()