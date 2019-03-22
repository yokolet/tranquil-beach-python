from .node import Node

class CopyWithRandom:
    def copyRandomList(self, head: 'Node') -> 'Node':
        head2 = Node(None, None, None)
        cur = head
        cache = {} # (key, value) = (cur, ref), copied instance
        prev = head2
        while cur:
            n = Node(cur.val, None, None)
            prev.next = n
            cache[cur.val] = n
            prev = n
            cur = cur.next
        cur = head
        cur2 = head2.next
        while cur:
            if cur.random:
                cur2.random = cache[cur.random.val]
            cur = cur.next
            cur2 = cur2.next
        return head2.next
