# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    @staticmethod
    def serialize(head):
        # {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
        cur = head
        stack = []
        while cur:
            if cur: stack.append(cur)
            cur = cur.next
        prev = None
        while stack:
            cur = stack.pop()
            tmp = {
                "$id": str(cur.val),
                "next": prev,
                "random": {"$ref": str(cur.random.val)},
                "val": cur.val
            }
            prev = tmp
        return prev