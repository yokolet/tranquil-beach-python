from .list_node import ListNode

class ReverseLinkedList:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, rev = head, None
        while cur:
            rev, rev.next, cur = cur, rev, cur.next
        return rev

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        prev, cur, next_ = None, head, None
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        return prev
