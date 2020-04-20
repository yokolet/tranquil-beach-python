from .tree_node import TreeNode

class BSTByPreorder:
    def bstFromPreorder(self, preorder: 'List[int]') -> TreeNode:
        def build(arr):
            if not arr: return None
            n = TreeNode(arr[0])
            if len(arr) == 1: return n
            idx = 1
            while idx < len(arr) and arr[idx] < arr[0]:
                idx += 1
            n.left = build(arr[1:idx])
            n.right = build(arr[idx:])
            return n
        return build(preorder)
