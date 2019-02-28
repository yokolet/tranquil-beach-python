class ValidBST:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def walk(root, lower, upper):
            if not root: return True
            if root.val > lower and root.val < upper:
                return walk(root.left, lower, root.val) and walk(root.right, root.val, upper)
            else:
                return False
        return walk(root, float('-inf'), float('inf'))

    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValid(root, smaller, bigger):
            if not root:
                return True
            if root.val > smaller and root.val < bigger:
                return isValid(root.left, smaller, root.val) and\
                        isValid(root.right, root.val, bigger)
            else:
                return False

        return isValid(root, float('-inf'), float('inf'))