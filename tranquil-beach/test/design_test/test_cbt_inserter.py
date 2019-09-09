import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from tree.tree_node import TreeNode
from tree.str2tree import Str2Tree
from tree.tree2str import Tree2Str
from design.cbt_inserter import CBTInserter

class TestCBTInserter(unittest.TestCase):
    def setUp(self):
        self.builder = Str2Tree()
        self.serializer = Tree2Str()

    def test_1(self):
        ops = ["CBTInserter","insert","get_root"]
        s = '1'
        root = self.builder.str2tree(s)
        params = [[root],[2],[]]
        expected = [None,1,'1(2)']
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            if op == "get_root":
                ret = getattr(func, op)(*param)
                result.append(self.serializer.tree2str(ret))
            else:
                result.append(getattr(func, op)(*param))
        self.assertEqual(expected, result)

    def test_2(self):
        ops = ["CBTInserter","insert","insert","get_root"]
        s = '1(2(4)(5))(3(6))'
        root = self.builder.str2tree(s)
        params = [[root],[7],[8],[]]
        expected = [None,3,4,'1(2(4(8))(5))(3(6)(7))']
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            if op == "get_root":
                ret = getattr(func, op)(*param)
                result.append(self.serializer.tree2str(ret))
            else:
                result.append(getattr(func, op)(*param))
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()