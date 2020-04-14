from .tree_node import TreeNode

class FlippedBinaryTree:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def walk(n1, n2):
            if not n1 and not n2: return True
            if not n1 or not n2: return False
            if n1.val != n2.val: return False
            return (walk(n1.left, n2.left) and walk(n1.right, n2.right)) or\
                (walk(n1.left, n2.right) and walk(n1.right, n2.left))
        return walk(root1, root2)