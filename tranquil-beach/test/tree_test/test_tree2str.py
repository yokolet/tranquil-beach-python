import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.tree2str import Tree2Str

class TestTree2Str(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.func = Tree2Str()

    def test_1(self):
        s = "1(2(3)(4))(5()(6))"
        root = self.builder.str2tree(s)
        self.assertEqual(self.func.tree2str(root), s)

if __name__ == '__main__':
    unittest.main()