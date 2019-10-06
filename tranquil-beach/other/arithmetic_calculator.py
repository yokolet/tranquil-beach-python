class ArithmeticCalculator:
    def calculate(self, s: str) -> int:
        last, v, acc, op = 0, 0, 0, '+'
        for i, c in enumerate(s):
            if c.isdigit():
                v = v*10 + int(c)
            if c in '+-*/' or i == len(s)-1:
                if op == '+':
                    acc += last
                    last = v
                elif op == '-':
                    acc += last
                    last = -v
                elif op == '*':
                    last *= v
                elif op =='/':
                    last = int(last / v)
                v = 0
                op = c
        return acc + last

    # solution below got maximum recursion depth exceeded in comparison error
    def calculate2(self, s: str) -> int:
        if not s: return 0

        def calc(expr, i, acc, op, last):
            sub = ''
            while i < len(expr) and expr[i].isdigit():
                sub += expr[i]
                i += 1
            v = int(sub)
            if op == '+':
                acc += last
            elif op == '-':
                acc += last
                v = -v
            elif op == '*':
                v *= last
            elif v != 0 and op =='/':
                v = int(last / v)

            if i == len(expr):
                return acc + v
            else:
                op = expr[i]
                return calc(expr, i+1, acc, op, v)

        expr = s.replace(' ', '')
        return calc(expr, 0, 0, None, 0)

