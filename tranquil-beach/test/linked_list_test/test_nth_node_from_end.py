import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.list_node import ListNode
from linked_list.nth_node_from_end import NthNodeFromEnd

class TestNthNodeFromEnd(unittest.TestCase):
    def setUp(self):
        self.func = NthNodeFromEnd()

    def test_1(self):
        head = ListNode.build([1, 2, 3, 4, 5])
        n = 2
        expected = '1 -> 2 -> 3 -> 5'
        result = self.func.removeNthFromEnd(head, n)
        self.assertEqual(ListNode.stringify(result), expected)

if __name__ == '__main__':
    unittest.main()