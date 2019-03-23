import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from linked_list.list_node import ListNode
from linked_list.palindrome_list import PalindromeList

class TestPalindromeList(unittest.TestCase):
    def setUp(self):
        self.func = PalindromeList()

    def test_1(self):
        head = ListNode.build([1, 2])
        self.assertFalse(self.func.isPalindrome(head))

    def test_2(self):
        head = ListNode.build([1, 2, 2, 1])
        self.assertTrue(self.func.isPalindrome(head))

if __name__ == '__main__':
    unittest.main()