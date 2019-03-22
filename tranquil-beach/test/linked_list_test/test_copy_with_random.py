import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.node import Node
from linked_list.copy_with_random import CopyWithRandom

class TestCopyWithRandom(unittest.TestCase):
    def setUp(self):
        self.func = CopyWithRandom()

    def test_1(self):
        input = {"$id":"1","next":{"$id":"2","next":None,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
        n1 = Node(1, None, None)
        n2 = Node(2, None, None)
        n1.next = n2
        n1.random = n2
        n2.random = n2
        print(Node.serialize(n1))
        result = self.func.copyRandomList(n1)
        self.assertEqual(Node.serialize(result), input)

if __name__ == '__main__':
    unittest.main()