import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.list_node import ListNode
from linked_list.reorder_list import ReorderList

class TestReorderList(unittest.TestCase):
    def setUp(self):
        self.func = ReorderList()

    def test_1(self):
        head = ListNode.build([1, 2, 3, 4])
        expected = '1 -> 4 -> 2 -> 3'
        self.func.reorderList(head)
        self.assertEqual(ListNode.stringify(head), expected)

    def test_2(self):
        head = ListNode.build([1, 2, 3, 4, 5])
        expected = '1 -> 5 -> 2 -> 4 -> 3'
        self.func.reorderList(head)
        self.assertEqual(ListNode.stringify(head), expected)

if __name__ == '__main__':
    unittest.main()