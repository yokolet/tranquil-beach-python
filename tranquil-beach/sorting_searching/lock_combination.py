class LockCombination:
    def openLock(self, deadends: 'List[str]', target: str) -> int:
        digits = {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        def nextCombinations(s):
            ary = []
            for i in range(4):
                ary += [s[:i]+x+s[i+1:] for x in digits[s[i]]]
            return ary

        if '0000' in deadends: return -1
        seen = set(deadends)
        seen.add(target)
        queue = [(target, 0)]
        while queue:
            cur, steps = queue.pop(0)
            if cur == '0000': return steps
            for d in nextCombinations(cur):
                if d not in seen:
                    seen.add(d)
                    queue.append((d, steps+1))
        return -1
