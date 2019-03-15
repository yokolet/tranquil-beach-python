import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.max_path_sum import MaxPathSum

class TestMaxPathSum(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = MaxPathSum()

    def test_1(self):
        s = "1(2)(3)"
        expected = 6
        root = self.builder.str2tree(s)
        result = self.func.maxPathSum(root)
        self.assertEqual(result, expected)

    def test_2(self):
        s = "-10(9)(20(15)(7))"
        expected = 42
        root = self.builder.str2tree(s)
        result = self.func.maxPathSum(root)
        self.assertEqual(result, expected)

    def test_3(self):
        s = "-3"
        expected = -3
        root = self.builder.str2tree(s)
        result = self.func.maxPathSum(root)
        self.assertEqual(result, expected)

    def test_4(self):
        s = "1(2)"
        expected = 3
        root = self.builder.str2tree(s)
        result = self.func.maxPathSum(root)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()