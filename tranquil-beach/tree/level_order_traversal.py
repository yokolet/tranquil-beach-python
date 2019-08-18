from .tree_node import TreeNode

class LevelOrderTraversal:
    def levelOrder(self, root: TreeNode) -> 'List[List[int]]':
        if not root: return []
        queue = [root]
        result = []
        while queue:
            result.append([])
            for _ in range(len(queue)):
                cur = queue.pop(0)
                result[-1].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result

    def levelOrder2(self, root: TreeNode) -> 'List[List[int]]':
        if not root: return []
        queue = [root]
        result = []
        while queue:
            tmp = []
            result.append([])
            for q in queue:
                result[-1].append(q.val)
                if q.left != None:
                    tmp.append(q.left)
                if q.right != None:
                    tmp.append(q.right)
            queue = tmp
        return result
