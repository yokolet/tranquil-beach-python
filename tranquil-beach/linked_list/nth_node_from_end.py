from .list_node import ListNode

class NthNodeFromEnd:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(None)
        root.next = head
        fast = root
        for _ in range(n):
            fast = fast.next
        cur = root
        while fast.next:
            fast = fast.next
            cur = cur.next
        cur.next = cur.next.next
        return root.next
