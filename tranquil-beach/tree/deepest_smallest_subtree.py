from .tree_node import TreeNode

class DeepestSmallestSubtree:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def walk(root: TreeNode, depth: int) -> (TreeNode, int):    # parent_node, depth
            if not root: return None, depth
            l_n, l_d = walk(root.left, depth+1)
            r_n, r_d = walk(root.right, depth+1)
            if l_d > r_d:
                return l_n, l_d
            elif r_d > l_d:
                return r_n, r_d
            else:
                return root, l_d
        node, _ = walk(root, 0)
        return node
