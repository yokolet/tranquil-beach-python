import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.serialize_deserialize import SerializeDeserialize, TreeNode

class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.func = SerializeDeserialize()

    def test_1(self):
        tree = '[1,2,3,null,null,4,5]'
        root = self.func.deserialize(tree)
        self.assertEquals(tree, self.func.serialize(root))

    def test_2(self):
        tree = '[5,2,3,null,null,2,4,3,1]'
        root = self.func.deserialize(tree)
        self.assertEquals(tree, self.func.serialize(root))

    def test_3(self):
        tree = '[]'
        root = self.func.deserialize(tree)
        self.assertEquals(tree, self.func.serialize(root))


if __name__ == '__main__':
    unittest.main()