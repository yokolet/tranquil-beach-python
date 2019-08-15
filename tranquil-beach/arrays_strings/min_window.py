from collections import defaultdict

class MinWindow:
    def minWindow(self, s: str, t: str) -> str:
        missing, left, min_left, min_right = len(t), 0, 0, float('inf')
        target = defaultdict(int)
        for c in t:
            target[c] += 1
        for right, c in enumerate(s, 1):
            if target[c] > 0:
                missing -= 1
            target[c] -= 1
            if missing == 0:
                while target[s[left]] < 0:
                    target[s[left]] += 1
                    left += 1
                if right - left < min_right - min_left:
                    min_left, min_right = left, right
        return '' if min_right == float('inf') else  s[min_left:min_right]

    def minWindow3(self, s: str, t: str) -> str:  # wrong answer
        result, left, target, counts = '', -1, defaultdict(int), {}
        for c in t:
            target[c] += 1
        for i in range(len(s)):
            if s[i] not in target: continue
            if left < 0: left = i
            counts[s[i]] = counts.get(s[i], 0) + 1
            if counts == target:
                tmp = s[left:i+1]
                if not result or len(result) > len(tmp):
                    result = tmp
                counts[s[left]] -= 1
                left += 1
                while left < len(s) and s[left] not in target:
                    left += 1
            elif counts[s[i]] > target[s[i]]:
                counts[s[i]] -= 1
                left += 1
                while left < len(s) and s[left] not in target:
                    left += 1
        return result

    def minWindow2(self, s: str, t: str) -> str:
        missing, left, min_left, min_right = len(t), 0, 0, float('inf')
        memo = defaultdict(int)
        for c in t:
            memo[c] += 1
        for right, c in enumerate(s):
            if memo[c] > 0:
                missing -= 1
            memo[c] -= 1
            if missing == 0:
                while memo[s[left]] < 0:
                    memo[s[left]] += 1
                    left += 1
                if right - left < min_right - min_left:
                    min_right, min_left = right, left
                memo[s[left]] += 1
                missing += 1
                left += 1
        return '' if min_right == float('inf') else s[min_left:min_right+1]
