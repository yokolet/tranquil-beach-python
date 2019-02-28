import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.valid_bst import ValidBST

class TestValidBST(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = ValidBST()

    def test_1(self):
        s = "2(1)(3)"
        expected = True
        root = self.builder.str2tree(s)
        self.assertEqual(self.func.isValidBST(root), expected)

    def test_2(self):
        s = "5(1)(4(3)(6))"
        expected = False
        root = self.builder.str2tree(s)
        self.assertEqual(self.func.isValidBST(root), expected)
    
    def test_3(self):
        s = "1(1)"
        expected = False
        root = self.builder.str2tree(s)
        self.assertEqual(self.func.isValidBST(root), expected)

if __name__ == '__main__':
    unittest.main()