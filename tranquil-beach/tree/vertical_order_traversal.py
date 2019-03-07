from collections import defaultdict

class VerticalOrderTraversal:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = [(root, 0)] # node, left(negative) or right(positive)
        result = defaultdict(list)
        while queue:
            node, lr = queue.pop(0)
            result[lr].append(node.val)
            if node.left:
                queue.append((node.left, lr - 1))
            if node.right:
                queue.append((node.right, lr + 1))
        return [result[k] for k in sorted(result.keys())]

    def verticalOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        dic = {}
        que = [(0, root)]
        while que:
            idx, node = que.pop(0)
            if idx not in dic:
                dic[idx] = []
            dic[idx].append(node.val)
            if node.left:
                que.append((idx - 1, node.left))
            if node.right:
                que.append((idx + 1, node.right))
        return [v for k, v in sorted(dic.items())]