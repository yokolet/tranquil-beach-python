class LevelOrderTraversal:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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

    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = [root]
        result = []
        while queue:
            n = len(queue)
            tmp = []
            while n > 0:
                cur = queue.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                n -= 1
            result.append(tmp)
        return result

