class LongestSubstring2Distinct:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, max_len, memo = 0, 0, {}
        for i, c in enumerate(s):
            memo[c] = i
            if len(memo) > 2:
                left = min(memo.values())
                del memo[s[left]]
                left += 1
            max_len = max(max_len, i-left+1)
        return max_len