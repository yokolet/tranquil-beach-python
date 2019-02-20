import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.list_node import ListNode
from linked_list.intersection import Intersection

class TestIntersection(unittest.TestCase):
    def setUp(self):
        self.func = Intersection()

    def test_1(self):
        c = ListNode(8)
        c.next = ListNode(4)
        c.next.next = ListNode(5)
        a = ListNode(4)
        a.next = ListNode(1)
        a.next.next = c
        b = ListNode(5)
        b.next = ListNode(0)
        b.next.next = ListNode(1)
        b.next.next.next = c
        result = self.func.getIntersectionNode(a, b)
        self.assertEqual(result, c)
    
    def test_2(self):
        a = ListNode(2)
        a.next = ListNode(6)
        a.next.next = ListNode(4)
        b = ListNode(1)
        b.next = ListNode(5)
        result = self.func.getIntersectionNode(a, b)
        self.assertIsNone(result)
    

if __name__ == '__main__':
    unittest.main()