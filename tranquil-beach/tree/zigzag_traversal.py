from .tree_node import TreeNode

class ZigzagTraversal:
    def zigzagLevelOrder(self, root: TreeNode) -> 'List[List[int]]':
        if not root: return []
        queue, result = [root], []
        lr = False
        while queue:
            tmp = []
            for _ in range(len(queue)):
                if lr:
                    node = queue.pop()
                    tmp.append(node.val)
                    if node.right: queue.insert(0, node.right)
                    if node.left: queue.insert(0, node.left)
                else:
                    node = queue.pop(0)
                    tmp.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            result.append(tmp)
            lr = not lr
        return result

