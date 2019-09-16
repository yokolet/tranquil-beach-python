from .node import Node
from collections import defaultdict

class CopyWithRandom:
    def copyRandomList(self, head: Node) -> Node:
        cache = defaultdict(lambda: Node(None, None, None))
        cache[None] = None  # to avoid if statement in the loop
        cur = head
        while cur:
            cache[cur].val = cur.val
            cache[cur].next = cache[cur.next]
            cache[cur].random = cache[cur.random]
            cur = cur.next
        return cache[head]

    def copyRandomList2(self, head: 'Node') -> 'Node':
        dummy = Node(None, None, None)
        cur, prev = head, dummy
        cache = {} # (key, value) = (cur, ref), copied instance
        while cur:
            prev.next = Node(cur.val, None, None)
            cache[cur.val] = prev.next
            cur, prev = cur.next, prev.next
        cur, copy = head, dummy.next
        while cur:
            if cur.random:
                copy.random = cache[cur.random.val]
            cur, copy = cur.next, copy.next
        return dummy.next
