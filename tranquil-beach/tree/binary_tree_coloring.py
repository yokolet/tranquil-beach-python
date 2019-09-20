from .tree_node import TreeNode

class BinaryTreeColoring:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def findX(root, x):
            if not root: return None
            if root.val == x: return root
            left = findX(root.left, x)
            right = findX(root.right, x)
            return left or right

        def count(root):
            if not root: return 0
            return 1+count(root.left)+count(root.right)

        node_x = findX(root, x)
        left = count(node_x.left)
        right = count(node_x.right)
        return max(n - (1 + left + right), left, right) > n // 2
