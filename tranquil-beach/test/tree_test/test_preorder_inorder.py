import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.tree2str import Tree2Str
from tree.preorder_inorder import PreorderInorder

class TestPreorderInorder(unittest.TestCase):
    def setUp(self):
        self.helper = Tree2Str()
        self.func = PreorderInorder()

    def test_1(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        expected = '3(9)(20(15)(7))'
        result = self.func.buildTree(preorder, inorder)
        self.assertEqual(self.helper.tree2str(result), expected)

    def test_2(self):
        preorder = []
        inorder = []
        expected = ''
        result = self.func.buildTree(preorder, inorder)
        self.assertEqual(self.helper.tree2str(result), expected)

if __name__ == '__main__':
    unittest.main()