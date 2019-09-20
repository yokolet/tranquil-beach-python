import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.binary_tree_coloring import BinaryTreeColoring

class TestBinaryTreeColoring(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = BinaryTreeColoring().btreeGameWinningMove

    def test_1(self):
        s, n, x = '1(2(4(8)(9))(5(10)(11)))(3(6)(7))', 11, 3
        expected = True
        root = self.builder.str2tree(s)
        self.assertTrue(self.func(root, n, x))

    def test_2(self):
        s, n, x = '1(2)(3)', 3, 2
        expected = True
        root = self.builder.str2tree(s)
        self.assertTrue(self.func(root, n, x))

    def test_3(self):
        s, n, x = '1(2)(3)', 3, 1
        expected = False
        root = self.builder.str2tree(s)
        self.assertFalse(self.func(root, n, x))

if __name__ == '__main__':
    unittest.main()