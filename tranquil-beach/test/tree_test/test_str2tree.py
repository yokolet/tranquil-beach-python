import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree

class TestStr2Tree(unittest.TestCase):
    def setUp(self):
        self.func = Str2Tree()

    def test_1(self):
        string = "4(2(3)(1))(6(5))"
        result = self.func.str2tree(string)
        self.assertEqual(result.val, 4)
        self.assertEqual(result.left.val, 2)
        self.assertEqual(result.left.left.val, 3)
        self.assertEqual(result.left.left.left, None)
        self.assertEqual(result.left.left.right, None)
        self.assertEqual(result.left.right.val, 1)
        self.assertEqual(result.right.val, 6)
        self.assertEqual(result.right.left.val, 5)
        self.assertEqual(result.right.left.right, None)

    def test_2(self):
        string = "1(2()(5))(3)"
        result = self.func.str2tree(string)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.left.val, 2)
        self.assertEqual(result.left.left, None)
        self.assertEqual(result.left.right.val, 5)
        self.assertEqual(result.right.val, 3)
        self.assertEqual(result.right.left, None)
        self.assertEqual(result.right.right, None)


if __name__ == '__main__':
    unittest.main()