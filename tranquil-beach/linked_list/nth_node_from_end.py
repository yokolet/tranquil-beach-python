from .list_node import ListNode

class NthNodeFromEnd:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        fast = dummy
        for _ in range(n):
            fast = fast.next
        cur = dummy
        while fast.next:
            fast = fast.next
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
