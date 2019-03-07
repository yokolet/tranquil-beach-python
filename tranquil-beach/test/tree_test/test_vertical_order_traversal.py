import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.vertical_order_traversal import VerticalOrderTraversal

class TestVerticalOrderTraversal(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = VerticalOrderTraversal()

    def test_1(self):
        s = '3(9)(20(15)(7))'
        expected = [
            [9],
            [3,15],
            [20],
            [7]
            ]
        root = self.builder.str2tree(s)
        self.assertEqual(self.func.verticalOrder(root), expected)

if __name__ == '__main__':
    unittest.main()