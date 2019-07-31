class LongestSubstringKDistinct:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, max_length, memo = 0, 0, {}
        for i, char in enumerate(s):
            memo[char] = i
            if len(memo) > k:
                left = min(memo.values())
                del memo[s[left]]
                left += 1
            if i - left + 1 > max_length:
                max_length = i - left + 1
        return max_length