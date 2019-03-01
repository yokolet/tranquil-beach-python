import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.bst_to_list import BSTToList

class TestBSTToList(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = BSTToList()

    def test_1(self):
        s = '4(2(1)(3))(5)'
        root = self.builder.str2tree(s)
        result = self.func.treeToDoublyList(root)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.right.val, 2)
        self.assertEqual(result.left.val, 5)
        self.assertEqual(result.right.right.val, 3)
        self.assertEqual(result.right.left.val, 1)

if __name__ == '__main__':
    unittest.main()