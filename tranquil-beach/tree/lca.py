from .tree_node import TreeNode

class Lca:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        if left:
            return left
        else:
            return right

    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            cur = stack.pop()
            if cur.left:
                parent[cur.left] = cur
                stack.append(cur.left)
            if cur.right:
                parent[cur.right] = cur
                stack.append(cur.right)
        parents = set()
        while p:
            parents.add(p)
            p = parent[p]
        while q not in parents:
            q = parent[q]
        return q

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def walk(root, result):
            if not root: return False, result
            left, result = walk(root.left, result)
            right, result = walk(root.right, result)
            mid = root == p or root == q
            if mid + left + right >= 2:
                result = root
            return mid or left or right, result
        result = None
        _, result = walk(root, result)
        return result