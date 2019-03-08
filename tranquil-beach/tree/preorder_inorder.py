from .tree_node import TreeNode

class PreorderInorder:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(p_iter, p_start, p_end):
            if p_start > p_end: return None
            val = next(p_iter)
            node = TreeNode(val)
            node.left = build(p_iter, p_start, idx_dict[val] - 1)
            node.right = build(p_iter, idx_dict[val]+ 1, p_end)
            return node
        idx_dict = {v: i for i, v in enumerate(inorder)}
        return build(iter(preorder), 0, len(preorder)-1)

    def buildTree2(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def inorder2dict(inorder):
            d = {}
            for idx, v in enumerate(inorder):
                d[v] = idx
            return d

        def arrays2tree(pre_iter, pre_start, pre_end, inor_dict):
            if pre_start > pre_end: return None
            val = next(pre_iter)
            node = TreeNode(val)
            idx = inor_dict[val]
            node.left = arrays2tree(pre_iter, pre_start, idx-1, inor_dict)
            node.right = arrays2tree(pre_iter, idx+1, pre_end, inor_dict)
            return node

        inorderDict = inorder2dict(inorder)
        return arrays2tree(iter(preorder), 0, len(inorder)-1, inorderDict)
