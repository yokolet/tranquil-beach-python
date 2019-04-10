class Node:
    def __init__(self, x, count):
        self.val = x
        self.left = None
        self.right = None
        self.count = count

class KthLargestBst:
    def __init__(self, k: int, nums: 'List[int]'):
        self.k = k - 1
        self.root = None
        for x in nums:
            self.root = self.insert(self.root, x)
    
    def insert(self, node: Node, x: int) -> Node:
        if not node: return Node(x, 0)
        elif node.val > x:
            node.left = self.insert(node.left, x)
        else:
            node.count += 1
            node.right = self.insert(node.right, x)
        return node

    def add(self, val: int) -> int:
        def findKth(node, count):
            if not node: return -1
            elif node.count == count: return node.val
            elif node.count > count:
                return findKth(node.right, count)
            else:
                return findKth(node.left, count - node.count - 1)
        self.root = self.insert(self.root, val)
        return findKth(self.root, self.k)