class InvalidParentheses:
    def removeInvalidParentheses(self, s: str) -> 'List[str]':
        def remove(s, left, right, parens):
            count = 0
            while right < len(s):
                if s[right] == parens[0]:
                    count += 1
                elif s[right] == parens[1]:
                    count -= 1
                
                if count >= 0:
                    right += 1
                    continue
                
                start = left
                while left <= right:
                    if s[left] == parens[1] and (left == start or s[left - 1] != parens[1]):
                        remove(s[:left] + s[left+1:], left, right, parens)
                    left += 1
                return

            if parens[1] == ')':
                remove(s[::-1], 0, 0, (')', '('))
            else:
                result.append(s[::-1])

        result = []
        remove(s, 0, 0, ('(', ')'))
        return result