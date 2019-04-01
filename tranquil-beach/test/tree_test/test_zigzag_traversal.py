import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.zigzag_traversal import ZigzagTraversal

class TestZigzagTraversal(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = ZigzagTraversal()

    def test_1(self):
        s = '3(9)(20(15)(7))'
        expected = [[3],[20,9],[15,7]]
        root = self.builder.str2tree(s)
        self.assertEqual(self.func.zigzagLevelOrder(root), expected)
    
    def test_2(self):
        s = '1(2(4))(3()(5))'
        expected = [[1],[3,2],[4,5]]
        root = self.builder.str2tree(s)
        self.assertEqual(self.func.zigzagLevelOrder(root), expected)

if __name__ == '__main__':
    unittest.main()