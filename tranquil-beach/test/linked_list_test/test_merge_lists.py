import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.list_node import ListNode
from linked_list.merge_lists import MergeLists

class TestMergeLists(unittest.TestCase):
    def setUp(self):
        self.func = MergeLists()

    def test_1(self):
        lists = [
            ListNode.build([1, 4, 5]),
            ListNode.build([1, 3, 4]),
            ListNode.build([2, 6])
        ]
        expected = '1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6'
        result = self.func.mergeKLists(lists)
        self.assertEqual(ListNode.stringify(result), expected)

if __name__ == '__main__':
    unittest.main()