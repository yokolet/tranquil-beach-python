import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.list_node import ListNode
from linked_list.twonumbers import TwoNumbers

class TestTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.func = TwoNumbers()

    def test_1(self):
        '''
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8 --- 342 + 465 = 807
        '''
        a = ListNode(2)
        a.next = ListNode(4)
        a.next.next = ListNode(3)
        b = ListNode(5)
        b.next = ListNode(6)
        b.next.next = ListNode(4)
        head = self.func.addTwoNumbers(a, b)
        cur, result = head, ''
        while cur:
            result = str(cur.val) + result
            cur = cur.next
        self.assertEqual(result, "807")

    def test_2(self):
        a = ListNode(9)
        a.next = ListNode(8)
        b = ListNode(1)
        head = self.func.addTwoNumbers(a, b)
        cur, result = head, ''
        while cur:
            result = str(cur.val) + result
            cur = cur.next
        self.assertEqual(result, "90")


if __name__ == '__main__':
    unittest.main()