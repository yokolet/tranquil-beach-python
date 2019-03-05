from .list_node import ListNode

class MergeLists:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        cur = head
        values = []
        for list_ in lists:
            while list_:
                cur.next = list_
                values.append(list_.val)
                list_ = list_.next
                cur = cur.next
        cur = head.next
        for v in sorted(values):
            cur.val = v
            cur = cur.next
        return head.next