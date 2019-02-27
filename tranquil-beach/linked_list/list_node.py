class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    @staticmethod
    def build(ary):
        head = ListNode(None)
        cur = head
        for v in ary:
            cur.next = ListNode(v)
            cur = cur.next
        return head.next

    @staticmethod
    def stringify(l):
        s = ''
        while l:
            s += str(l.val)
            l = l.next
            if l: s += ' -> '
        return s