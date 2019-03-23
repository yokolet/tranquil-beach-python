from .list_node import ListNode

class PalindromeList:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, rev = head, head, None
        while fast and fast.next: # find half point while reversing first half
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev: # compare reversed first half and last half
            if rev.val != slow.val: return False
            slow = slow.next
            rev = rev.next
        return True