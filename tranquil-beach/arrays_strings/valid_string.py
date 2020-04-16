class ValidString:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0
        for c in s:
            if c == '(': left_min += 1
            else: left_min -= 1
            if c in ['(', '*']: left_max += 1
            else: left_max -= 1
            if left_max < 0: break
            left_min = max(left_min, 0)
        return left_min == 0
    
    # TLE
    def checkValidString2(self, s: str) -> bool:
        if not s: return True
        if s[0] == ')': return False
        queue = []
        if s[0] == '(':
            queue.append((0, 1))
        elif s[0] == '*':
            queue.append((0, 1))
            queue.append((0, 0))
        while queue:
            idx, cur = queue.pop(0)
            if cur < 0: continue
            if idx+1 == len(s):
                if cur == 0: return True
                else: continue
            if s[idx+1] == '(':
                queue.append((idx+1, cur+1))
            elif s[idx+1] == ')':
                queue.append((idx+1, cur-1))
            elif s[idx+1] == '*':
                queue.append((idx+1, cur+1))
                queue.append((idx+1, cur-1))
                queue.append((idx+1, cur))
        return False
