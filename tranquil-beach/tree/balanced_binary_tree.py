from .tree_node import TreeNode

class BalancedBinaryTree:
    def isBalanced(self, root: TreeNode) -> bool:
        def walk(root: TreeNode) -> (int, bool):
            if not root: return 0, True
            l_h, l_ret = walk(root.left)
            r_h, r_ret = walk(root.right)
            if not l_ret or not r_ret or abs(l_h - r_h) > 1:
                return l_h, False
            return 1 + max(l_h, r_h), True
        _, ret = walk(root)
        return ret