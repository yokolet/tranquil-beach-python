from .list_node import ListNode

class TwoNumbers:
    def addTwoNumbers(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        if not l1 or not l2:
            return l1 or l2
        head = l1
        carry = 0
        while l1 and l2:
            carry, rem = divmod(l1.val + l2.val + carry, 10)
            l1.val = rem
            cur, l1, l2 = l1, l1.next, l2.next
        cur.next = l1 or l2
        while carry != 0:
            if not cur.next:
                cur.next = ListNode(carry)
                break
            else:
                carry, rem = divmod(cur.next.val + carry, 10)
                cur.next.val = rem
                cur = cur.next
        return head