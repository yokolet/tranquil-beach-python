import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.tree2str import Tree2Str
from tree.delete_nodes import DeleteNodes

class TestDeleteNodes(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree().str2tree
        self.serializer = Tree2Str().tree2str
        self.func = DeleteNodes().delNodes

    def test_1(self):
        s, target = "1(2(4)(5))(3(6)(7))", [3,5]
        expected = ["1(2(4))","6","7"]
        root = self.builder(s)
        result = self.func(root, target)
        result = [self.serializer(t) for t in result]
        self.assertCountEqual(result, expected)

    def test_2(self):
        s, target = "1(2(4)(5))(3(6)(7))", [1,3,5]
        expected = ["2(4)","6","7"]
        root = self.builder(s)
        result = self.func(root, target)
        result = [self.serializer(t) for t in result]
        self.assertCountEqual(result, expected)

if __name__ == '__main__':
    unittest.main()