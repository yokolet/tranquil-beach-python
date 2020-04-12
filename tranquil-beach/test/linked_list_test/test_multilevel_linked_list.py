import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.multilevel_linked_list import MultilevelLinkedList, Node

class TestMultilevelLinkedList(unittest.TestCase):
    def setUp(self):
        self.func = MultilevelLinkedList().flatten

    def test_1(self):
        # head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
        nodes = {}
        for i in range(1, 13):
            nodes[i] = Node(i)
        nodes[1].next = nodes[2]
        nodes[2].prev = nodes[1]
        nodes[2].next = nodes[3]
        nodes[3].prev = nodes[2]
        nodes[3].next = nodes[4]
        nodes[4].prev = nodes[3]
        nodes[4].next = nodes[5]
        nodes[5].prev = nodes[4]
        nodes[5].next = nodes[6]
        nodes[6].prev = nodes[5]
        nodes[3].child = nodes[7]
        nodes[7].next = nodes[8]
        nodes[8].prev = nodes[7]
        nodes[8].next = nodes[9]
        nodes[9].prev = nodes[8]
        nodes[9].next = nodes[10]
        nodes[10].prev = nodes[9]
        nodes[8].child = nodes[11]
        nodes[11].next = nodes[12]
        nodes[12].prev = nodes[11]
        head = self.func(nodes[1])
        expected = [1,2,3,7,8,11,12,9,10,4,5,6]
        result = []
        cur = head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        self.assertEqual(expected, result)
    
    def test_2(self):
        # head = [1,2,null,3]
        nodes = {}
        for i in range(1, 4):
            nodes[i] = Node(i, None, None, None)
        nodes[1].next = nodes[2]
        nodes[2].prev = nodes[1]
        nodes[1].child = nodes[3]
        head = self.func(nodes[1])
        expected = [1,3,2]
        result = []
        cur = head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        self.assertEqual(expected, result)

    def test_3(self):
        head = None
        head = self.func(head)
        expected = []
        result = []
        cur = head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
