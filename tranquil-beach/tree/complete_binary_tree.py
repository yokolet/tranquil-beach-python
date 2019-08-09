from .tree_node import TreeNode

class CompleteBinaryTree:
    def isCompleteTree(self, root: TreeNode) -> bool:
        def walk(root):
            if not root: return 0, 0, True
            l_min, l_max, l_ret = walk(root.left)
            r_min, r_max, r_ret = walk(root.right)
            ret = l_ret and r_ret
            if r_max > l_max:
                ret = False
            elif r_max+1 < l_max:
                ret = False
            elif l_min != l_max and (r_min != r_max or r_max != l_min):
                ret = False
            return 1+min(l_min, r_min), 1+max(l_max, r_max), ret
        _, _, ret = walk(root)
        return ret
