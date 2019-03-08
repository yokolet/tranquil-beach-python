class InvalidParentheses:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def remove(s, last_i, last_j, parens, result):
            i, count = last_i, 0
            while i < len(s):
                if s[i] == parens[0]:
                    count += 1
                elif s[i] == parens[1]:
                    count -= 1
                
                if count >= 0:
                    i += 1
                    continue
                
                j = last_j
                while j <= i:
                    if s[j] == parens[1] and (j == last_j or s[j - 1] != s[j]):
                        remove(s[:j] + s[j+1:], i, j, parens, result)
                    j += 1
                return

            if parens[1] == ')':
                remove(s[::-1], 0, 0, (')', '('), result)
            else:
                result.append(s[::-1])

        result = []
        remove(s, 0, 0, ('(', ')'), result)
        return result