class LongestSubstring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_length, memo = 0, 0, {} # char to index map
        for i in range(len(s)):
            if s[i] in memo:
                left = max(left, memo[s[i]])    
            max_length = max(max_length, i - left + 1)
            memo[s[i]] = i + 1
        return max_length

    def lengthOfLongestSubstring2(self, s: 'str') -> 'int':
        curr_substring = ''
        current_max = 0
        for c in s:
            if c not in curr_substring:
                curr_substring += c
                if len(curr_substring) > current_max:
                    current_max = len(curr_substring)
            else:
                curr_substring += c
                idx = curr_substring.find(c)
                curr_substring = curr_substring[idx+1:]
        return current_max