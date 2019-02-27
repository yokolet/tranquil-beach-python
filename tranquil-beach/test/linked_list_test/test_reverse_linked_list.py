import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.list_node import ListNode
from linked_list.reverse_linked_list import ReverseLinkedList

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.func = ReverseLinkedList()

    def test_1(self):
        # Input: 1->2->3->4->5->NULL
        # Output: 5->4->3->2->1->NULL
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        result = self.func.reverseList(head)
        self.assertEqual(result.val, 5)
        self.assertEqual(result.next.val, 4)

if __name__ == '__main__':
    unittest.main()