from .list_node import ListNode

class ReorderList:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        slow, fast = head, head
        while fast and fast.next: # find half point
            slow, fast = slow.next, fast.next.next
        slow.next, slow, rev = None, slow.next, None
        while slow:
            rev, rev.next, slow = slow, rev, slow.next
        cur = head
        while head and rev:
            head.next, rev.next, head, rev = rev, head.next, head.next, rev.next

    def reorderList2(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        slow, fast = head, head
        while fast and fast.next: # find half point
            slow, fast = slow.next, fast.next.next
        rev, cur, tmp = None, slow.next, None
        slow.next = None
        while cur: # reverse last half
            tmp = cur.next
            cur.next = rev
            rev = cur
            cur = tmp
        cur = head
        while rev:
            tmp, tmp2 = cur.next, rev.next
            cur.next = rev
            rev.next = tmp
            cur = tmp
            rev = tmp2

        
    def reorderList2(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        pre, slow.next, slow = None, None, slow.next
        while slow:
            slow.next, pre, slow = pre, slow, slow.next
        while head and pre:
            head.next, head, pre.next, pre = pre, head.next, head.next, pre.next
