import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.list_node import ListNode
from linked_list.merge_two_lists import MergeTwoLists

class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.func = MergeTwoLists().mergeTwoLists

    def test_1(self):
        l1 = ListNode.build([1, 2, 4])
        l2 = ListNode.build([1, 3, 4])
        expected = '1 -> 1 -> 2 -> 3 -> 4 -> 4'
        result = self.func(l1, l2)
        self.assertEquals(ListNode.stringify(result), expected)

if __name__ == '__main__':
    unittest.main()