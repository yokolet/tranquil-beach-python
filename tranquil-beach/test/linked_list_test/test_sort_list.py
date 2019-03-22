import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.list_node import ListNode
from linked_list.sort_list import SortList

class TestSortList(unittest.TestCase):
    def setUp(self):
        self.func = SortList()

    def test_1(self):
        head = ListNode.build([4, 2, 1, 3])
        expected = "1 -> 2 -> 3 -> 4"
        result = self.func.sortList(head)
        self.assertEqual(ListNode.stringify(result), expected)

    def test_2(self):
        head = ListNode.build([-1, 5, 3, 4, 0])
        expected = "-1 -> 0 -> 3 -> 4 -> 5"
        result = self.func.sortList(head)
        self.assertEqual(ListNode.stringify(result), expected)

if __name__ == '__main__':
    unittest.main()