import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from tree.tree_node import TreeNode

class SerializeDeserialize:
    def serialize(self, root: TreeNode) -> str:
        if not root: return ''
        result, queue = [], [root]
        while queue:
            cur = queue.pop(0)
            result.append(str(cur.val) if cur else 'null')
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)
        while result[-1] and result[-1] == 'null':
            result.pop()
        return ','.join(result)

    def deserialize(self, data: str) -> TreeNode:
        if not data or data == '': return None
        data = data.split(',')
        root = TreeNode(data[0])
        idx, queue = 0, [root]
        while queue:
            cur = queue.pop(0)
            if idx*2+1 < len(data) and data[idx*2+1] != 'null':
                cur.left = TreeNode(data[idx*2+1])
                queue.append(cur.left)
            if idx*2+2 < len(data) and data[idx*2+2] != 'null':
                cur.right = TreeNode(data[idx*2+2])
                queue.append(cur.right)
            idx += 1
        return root