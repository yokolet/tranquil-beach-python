from .list_node import ListNode

class SortList:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        def merge(l1, l2):
            head_ = ListNode(None)
            l0 = head_
            while l1 and l2:
                if l1.val < l2.val:
                    l0.next, l1 = l1, l1.next
                else:
                    l0.next, l2 = l2, l2.next
                l0 = l0.next
            if l1: l0.next = l1
            elif l2: l0.next = l2
            return head_.next
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast, prev = slow.next, fast.next.next, slow
        prev.next = None
        return merge(self.sortList(head), self.sortList(slow))
