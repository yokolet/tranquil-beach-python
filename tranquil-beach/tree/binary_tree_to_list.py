class BinaryTreeToList:    
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        def walk(root, prev):
            if not root: return prev
            prev = walk(root.right, prev)
            prev = walk(root.left, prev)
            root.right = prev
            root.left = None
            return root
        walk(root, None)

    def flatten2(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        stack = [root]
        prev = None
        while stack:
            cur = stack.pop()
            if prev:
                prev.right = cur
                prev.left = None
            prev = cur
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)