class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __repr__(self):
        return '<Node val={} prev={} next={} child={}>'.format(self.val, self.prev != None, self.next != None, self.child != None)

class MultilevelLinkedList:
    def flatten(self, head: Node) -> Node:
        def walk(prev, cur):
            if not cur: return prev
            cur.prev = prev
            prev.next = cur
            succ = cur.next
            tail = walk(cur, cur.child)
            cur.child = None
            return walk(tail, succ)
            
        if not head: return head
        dummy = Node(None, None, head, None)
        walk(dummy, head)
        dummy.next.prev = None
        return dummy.next

    def flatten2(self, head: Node) -> Node:
        if not head: return head
        dummy = Node(None, None, head, None)
        stack = []
        stack.append(head)
        prev = dummy
        while stack:
            cur = stack.pop()
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            prev.next = cur
            cur.prev = prev
            prev = cur
        dummy.next.prev = None
        return dummy.next
