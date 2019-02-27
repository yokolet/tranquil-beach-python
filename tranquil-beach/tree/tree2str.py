class Tree2Str:
    def tree2str(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def walk(root, result):
            if not root: return result
            result += str(root.val)
            if root.left or root.right:
                result += "("
                result = walk(root.left, result)
                result += ")"
                if root.right:
                    result += "("
                    result = walk(root.right, result)
                    result += ")"
            return result
        return walk(root, "")