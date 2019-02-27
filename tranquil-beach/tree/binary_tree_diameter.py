class BinaryTreeDiameter:
    def diameterOfBinaryTree(self, root: 'TreeNode') -> int:
        def walk(root: 'TreeNode') -> (int, int): # hegiht, diameter
            if not root: return 0, 0
            l_h, l_d = walk(root.left)
            r_h, r_d = walk(root.right)
            h = 1 + max(l_h, r_h)
            d = max(l_h + r_h, l_d, r_d)
            return h, d

        _, d = walk(root)
        return d

    def diameterOfBinaryTree2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def walk(root):
            if not root:
                return 0, 0
            else:
                l_depth, l_diam = walk(root.left)
                r_depth, r_diam = walk(root.right)
                depth = max(l_depth, r_depth) + 1
                diam = max(l_depth + r_depth, l_diam, r_diam)
                return depth, diam
        _, diameter = walk(root)
        return diameter