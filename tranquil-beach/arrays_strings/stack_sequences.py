class StackSequences:
    def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> bool:
        p, stack = 0, []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while p < len(popped) and len(stack) > 0 and stack[-1] == popped[p]:
                stack.pop()
                p += 1
        return len(stack) == 0
