class ReverseStrInParen:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)

        def walk(idx):
            result = ''
            while idx < n:
                if idx < n and s[idx] == '(':
                    idx += 1
                    idx, tmp = walk(idx)
                    result += tmp
                if idx < n and s[idx] == ')':
                    idx += 1
                    return (idx, result[::-1])
                if idx < n and s[idx] not in ['(', ')']:
                    result += s[idx]
                    idx += 1
            return (idx, result)

        _ ,  result = walk(0)
        return result
