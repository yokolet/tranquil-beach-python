import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.binary_tree_paths import TreePath

class TestTreePath(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = TreePath()

    def test_1(self):
        root = self.builder.str2tree("1(2()(5))(3)")
        expected = ["1->2->5", "1->3"]
        self.assertEqual(self.func.binaryTreePaths(root), expected)

if __name__ == '__main__':
    unittest.main()