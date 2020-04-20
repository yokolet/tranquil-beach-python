import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.tree2str import Tree2Str
from tree.bst_by_preorder import BSTByPreorder

class TestBSTByPreorder(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = BSTByPreorder().bstFromPreorder

    def test_1(self):
        preorder = [8,5,1,7,10,12]
        s = '8(5(1)(7))(10()(12))'
        expected = self.builder.str2tree(s)
        result = self.func(preorder)
        self.assertEqual(Tree2Str().tree2str(result), Tree2Str().tree2str(expected))

    def test_2(self):
        preorder = [4,2]
        s = '4(2)'
        expected = self.builder.str2tree(s)
        result = self.func(preorder)
        self.assertEqual(Tree2Str().tree2str(result), Tree2Str().tree2str(expected))

if __name__ == '__main__':
    unittest.main()
