import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.right_view import RightView

class TestRightView(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = RightView()

    def test_1(self):
        s = '1(2()(5))(3()(4))'
        expected = [1, 3, 4]
        root = self.builder.str2tree(s)
        self.assertEqual(self.func.rightSideView(root), expected)

if __name__ == '__main__':
    unittest.main()