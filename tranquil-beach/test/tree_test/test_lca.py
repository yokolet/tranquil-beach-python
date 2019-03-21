import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.lca import Lca

class TestLca(unittest.TestCase):
    def setUp(self):
        self.func = Lca()

    def build(self, array, p, q):
        nodes = {}
        for v in array:
            if v != None:
                nodes[v] = TreeNode(v)
        return nodes, nodes[p], nodes[q]

    def test_1(self):
        nodes, p, q = self.build([3,5,1,6,2,0,8,None,None,7,4], 5, 1)
        nodes[3].left, nodes[3].right = nodes[5], nodes[1]
        nodes[5].left, nodes[5].right = nodes[6], nodes[2]
        nodes[1].left, nodes[1].right = nodes[0], nodes[8]
        nodes[2].left, nodes[2].right = nodes[7], nodes[4]
        expected = 3
        self.assertEqual(self.func.lowestCommonAncestor(nodes[3], p, q).val, expected)

    def test_2(self):
        nodes, p, q = self.build([3,5,1,6,2,0,8,None,None,7,4], 5, 4)
        nodes[3].left, nodes[3].right = nodes[5], nodes[1]
        nodes[5].left, nodes[5].right = nodes[6], nodes[2]
        nodes[1].left, nodes[1].right = nodes[0], nodes[8]
        nodes[2].left, nodes[2].right = nodes[7], nodes[4]
        expected = 5
        self.assertEqual(self.func.lowestCommonAncestor(nodes[3], p, q).val, expected)

if __name__ == '__main__':
    unittest.main()