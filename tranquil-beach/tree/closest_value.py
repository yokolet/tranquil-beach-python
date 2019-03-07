from .tree_node import TreeNode

class ClosestValue:
    def closestValue(self, root: 'TreeNode', target: 'float') -> 'int':
        result = root.val
        if target < root.val and root.left is not None:
            result = self.closestValue(root.left, target)
        elif target > root.val and root.right is not None:
            result = self.closestValue(root.right, target)

        if abs(result - target) < abs(root.val - target):
            return result

        return root.val
    
    def closestValue2(self, root: TreeNode, target: float) -> int:
        cur = root
        result = cur.val
        while cur:
            if abs(result - target) > abs(cur.val - target):
                result = cur.val
            if cur.val < target:
                cur = cur.right
            elif cur.val > target:
                cur = cur.left
            else:
                break
        return result
            