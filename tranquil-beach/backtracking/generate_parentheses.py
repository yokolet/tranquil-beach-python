class GenerateParentheses:
    def generateParenthesis(self, n: int) -> 'List[str]':
        result, queue = [], [('(', n-1, n)]
        while queue:
            p, left, right = queue.pop(0)
            if left == 0 and right == 0:
                result.append(p)
            if left > 0:
                queue.append((p+'(', left-1, right))
            if right > 0 and left < right:
                queue.append((p+')', left, right-1))
        return result
