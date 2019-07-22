from .list_node import ListNode

class MergeTwoLists:
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1: cur.next = l1
        elif l2: cur.next = l2
        return dummy.next
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        elif not l2: return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2