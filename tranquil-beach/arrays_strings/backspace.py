class Backspace:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def edited(w):
            stack = []
            for c in w:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return stack
        
        return edited(S) == edited(T)
