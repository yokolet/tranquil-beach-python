from collections import defaultdict

class MinWindow:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
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
