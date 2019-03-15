import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from design.bst_iterator import BSTIterator

class TestBSTIterator(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()

    def test_1(self):
        s = '7(3)(15(9)(20))'
        root = self.builder.str2tree(s)
        bstIter = BSTIterator(root)
        self.assertEqual(bstIter.next(), 3)
        self.assertEqual(bstIter.next(), 7)
        self.assertTrue(bstIter.hasNext())
        self.assertEqual(bstIter.next(), 9)
        self.assertTrue(bstIter.hasNext())
        self.assertEqual(bstIter.next(), 15)
        self.assertTrue(bstIter.hasNext())
        self.assertEqual(bstIter.next(), 20)
        self.assertFalse(bstIter.hasNext())



if __name__ == '__main__':
    unittest.main()