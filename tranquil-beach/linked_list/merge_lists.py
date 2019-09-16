from .list_node import ListNode

class MergeLists:
    def mergeKLists(self, lists: 'List[ListNode]') -> ListNode:
        dummy = ListNode(None)
        cur = dummy
        values = []
        for list_ in lists:
            while list_:
                cur.next = list_
                values.append(list_.val)
                list_ = list_.next
                cur = cur.next
        cur = dummy.next
        for v in sorted(values):
            cur.val = v
            cur = cur.next
        return dummy.next
