import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.complete_tree_count import CompleteTreeCount

class TestCompleteTreeCount(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = CompleteTreeCount().countNodes

    def test_1(self):
        s = "1(2(4)(5))(3(6))"
        root = self.builder.str2tree(s)
        expected = 6
        self.assertEqual(expected, self.func(root))

    def test_2(self):
        s = "1(2)(3)"
        root = self.builder.str2tree(s)
        expected = 3
        self.assertEqual(expected, self.func(root))

    def test_3(self):
        s = "1(2(4))(3)"
        root = self.builder.str2tree(s)
        expected = 4
        self.assertEqual(expected, self.func(root))

if __name__ == '__main__':
    unittest.main()