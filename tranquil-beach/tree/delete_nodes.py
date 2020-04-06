from .tree_node import TreeNode

class DeleteNodes:
    def delNodes(self, root: TreeNode, to_delete: 'List[int]') -> 'List[TreeNode]':
        target = set(to_delete)
        roots = []
        if root.val not in target: roots.append(root)
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
                if cur.left.val in target: cur.left = None
            if cur.right:
                queue.append(cur.right)
                if cur.right.val in target: cur.right = None
            if cur.val in target:
                if cur.left: roots.append(cur.left)
                if cur.right: roots.append(cur.right)
        return roots

    def delNodes2(self, root: TreeNode, to_delete: 'List[int]') -> 'List[TreeNode]':
        def walk(n):
            if not n: return
            walk(n.left)
            walk(n.right)
            if n.left and n.left.val in to_delete:
                if n.left.left: roots.append(n.left.left)
                if n.left.right: roots.append(n.left.right)
                n.left = None
            if n.right and n.right.val in to_delete:
                if n.right.left: roots.append(n.right.left)
                if n.right.right: roots.append(n.right.right)
                n.right = None
            return
        to_delete = set(to_delete)
        roots = []
        walk(root)
        if root.val not in to_delete:
            roots.append(root)
        else:
            if root.left and root.left.val not in to_delete:
                roots.append(root.left)
            if root.right and root.right.val not in to_delete:
                roots.append(root.right)
        return roots