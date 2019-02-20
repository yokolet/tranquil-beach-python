from .tree_node import TreeNode

class Str2Tree:
    def str2tree(self, s: 'str') -> 'TreeNode':
        if not s: return None
        def walk(s, index, size):
            root = TreeNode(None)
            start = index
            while index < size:
                if s[index] == '(':
                    index += 1
                    if root.left == None:
                        root.left, index = walk(s, index, size)
                    else:
                        root.right, index = walk(s, index, size)
                        if root.left.val == None: root.left = None
                elif s[index] == ')':
                    index += 1
                    return root, index
                elif s[index] == '-':
                    index += 1
                else:
                    while index < size and str.isdigit(s[index]):
                        index += 1
                    root.val = int(s[start:index])
            return root, index
        root, _ = walk(s, 0, len(s))
        return root                    