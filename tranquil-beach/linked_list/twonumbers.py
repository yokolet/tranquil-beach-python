from .list_node import ListNode

class TwoNumbers:
     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return l1 or l2
        head, carry = l1, 0
        while l1 and l2:
            carry, rem = divmod(carry + l1.val + l2.val, 10)
            l1.val = rem
            cur, l1, l2 = l1, l1.next, l2.next
        cur.next = l1 or l2
        while carry and cur.next:
            carry, rem = divmod(carry + cur.next.val, 10)
            cur.next.val = rem
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return head