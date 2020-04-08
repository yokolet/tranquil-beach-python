import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.list_node import ListNode
from linked_list.middle_node import MiddleNode

class TestNthNodeFromEnd(unittest.TestCase):
    def setUp(self):
        self.func = MiddleNode().middleNode

    def test_1(self):
        head = ListNode.build([1, 2, 3, 4, 5])
        expected = 3
        result = self.func(head)
        self.assertEqual(result.val, expected)

    def test_2(self):
        head = ListNode.build([1,2,3,4,5,6])
        expected = 4
        result = self.func(head)
        self.assertEqual(result.val, expected)

if __name__ == '__main__':
    unittest.main()
