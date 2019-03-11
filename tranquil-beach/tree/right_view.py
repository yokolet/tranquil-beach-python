from .tree_node import TreeNode

class RightView:
    def rightSideView(self, root: TreeNode) -> 'List[int]':
        depth, result = -1, []
        if not root: return result
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if depth < level:
                result.append(node.val)
                depth = level
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))
        return result

            

