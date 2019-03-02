class ValidParentheses:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in pairs:
                # closing paren
                if len(stack) > 0 and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
