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
        head = ListNode.build([1, 2, 3, 4, 5])
        expected = '5 -> 4 -> 3 -> 2 -> 1'
        result = self.func.reverseList(head)
        self.assertEqual(result.val, 5)
        self.assertEqual(result.next.val, 4)
        self.assertEqual(ListNode.stringify(result), expected)

if __name__ == '__main__':
    unittest.main()