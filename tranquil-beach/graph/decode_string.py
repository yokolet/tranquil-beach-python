class DecodeString:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                sub = ''
                while stack and stack[-1] != '[':
                    sub = stack.pop() + sub
                stack.pop()
                d = ''
                while stack and stack[-1].isdigit():
                    d = stack.pop() + d
                stack.append(sub * int(d))
        return ''.join(stack)

    def decodeString3(self, s: str) -> str:
        stack = []
        d, a = '', ''
        for c in s:
            if c.isdigit():
                d += c
            elif c.isalpha():
                a += c
            elif c == '[':
                stack.append(a)
                stack.append(int(d))
                d, a = '', ''
            elif c == ']':
                prev_d = stack.pop()
                prev_a = stack.pop()
                a = prev_a + a * prev_d
        return a

    def decodeString2(self, s: str) -> str:
        def walk(s):
            d, a = '', ''
            result = ''
            while s:
                if s[0].isdigit():
                    d += s[0]
                    s = s[1:]
                elif s[0] == '[':
                    s, ret = walk(s[1:])
                    result += ret * int(d)
                    d = ''
                elif s[0].isalpha():
                    a += s[0]
                    s = s[1:]
                else: # ']'
                    return s[1:], a + result
            return '', result + a
        _, a = walk(s)
        return a
