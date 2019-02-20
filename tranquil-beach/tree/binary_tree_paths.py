from .tree_node import TreeNode

class TreePath:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def walk(root, path, result):
            path += str(root.val)
            if not root.left and not root.right:
                result.append(path)
            if root.left:
                walk(root.left, path+'->', result)
            if root.right:
                walk(root.right, path+'->', result)
        result = []
        if not root: return result
        walk(root, '', result)
        return result
