class LongestSubstringKDistinct:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, max_len, memo = 0, 0, {}
        for i, char in enumerate(s):
            memo[char] = i
            if len(memo) > k:
                left = min(memo.values())
                del memo[s[left]]
                left += 1
            max_len = max(max_len, i-left+1)
        return max_len