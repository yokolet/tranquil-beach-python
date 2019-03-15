from .tree_node import TreeNode

class MaxPathSum:
    def maxPathSum(self, root: TreeNode) -> int:
        def walk(root: TreeNode, max_sofar: int) -> (int, int): # max_sofar, val for upper stack
            if not root: return max_sofar, 0
            max_sofar, l_max = walk(root.left, max_sofar)
            max_sofar, r_max = walk(root.right, max_sofar)
            max_sofar = max(max_sofar, root.val + l_max + r_max)
            return max_sofar, max(root.val + max(l_max, r_max), 0)
        max_value, _ = walk(root, float('-inf'))
        return max_value
