import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from tree.tree_node import TreeNode

class CBTInserter:
    
    def __init__(self, root: TreeNode):
        self.root = root
        self.memo = []
        queue = [root]
        while queue:
            cur = queue.pop(0)
            self.memo.append(cur)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    
    def insert(self, v: int) -> int:
        n = len(self.memo)
        p_node = self.memo[(n-1)//2]
        if n % 2 == 1: # adds left child
            p_node.left = TreeNode(v)
            self.memo.append(p_node.left)
        else:          # adds right child
            p_node.right = TreeNode(v)
            self.memo.append(p_node.right)
        return p_node.val
        
    def get_root(self) -> TreeNode:
        return self.root