from .tree_node import TreeNode

class BSTToList:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def walk(root):
            if not root: return None, None
            if (not root.left) and (not root.right): return root, root

            ll, lr = walk(root.left)
            rl, rr = walk(root.right)

            root.left = lr
            root.right = rl
            if lr: lr.right = root
            if rl: rl.left = root

            left = ll if ll else root
            right = rr if rr else root
            return left, right

        left, right = walk(root)
        if left: left.left = right
        if right: right.right = left
        return left

    def treeToDoublyList2(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        cur, first, pre = root, None, None
        while cur:
            if not cur.left:
                if not first:
                    first = cur
                cur.left = pre
                if pre:
                    pre.right = cur
                pre = cur
                cur = cur.right
            else:
                left = cur.left
                while left.right and left.right != cur:
                    left = left.right
                if not left.right:
                    left.right = cur
                    cur = cur.left
                else:
                    cur.left = pre
                    pre = cur
                    cur = cur.right
        pre.right = first
        first.left = pre
        return first

    def treeToDoublyList3(self, root: 'TreeNode') -> 'TreeNode':
        if not root: return
        head = TreeNode(None)
        prev = head
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right,prev = prev, node, node
            node = node.right
        head.right.left, prev.right = prev, head.right
        return head.right