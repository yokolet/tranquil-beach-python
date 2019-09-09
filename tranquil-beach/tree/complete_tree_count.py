from .tree_node import TreeNode

class CompleteTreeCount:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def height(root):
            if not root: return 0
            return 1 + height(root.left)
        
        l_h = height(root)
        r_h = 1 + height(root.right)
        if l_h == r_h:
            return 2 ** (l_h - 1) + self.countNodes(root.right)
        else:
            return 2 ** (r_h - 1) + self.countNodes(root.left)

    def countNodes2(self, root: TreeNode) -> int:
        if not root: return 0
        count = 0
        queue = [root]
        while queue:
            count += len(queue)
            for i in range(len(queue)):
                n = queue.pop(0)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
        return count