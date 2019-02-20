from .list_node import ListNode

class Intersection:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        curA, curB, lenA, lenB = headA, headB, 0, 0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        
        curA, curB = headA, headB
        if lenA > lenB:
            for _ in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for _ in range(lenB-lenA):
                curB = curB.next
        
        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA

'''
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        cur_a = headA
        cur_b = headB
        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB
            cur_b = cur_b.next if cur_b else headA
        return cur_a
'''