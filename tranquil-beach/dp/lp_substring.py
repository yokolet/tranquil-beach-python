class LongestPalindromicSubstring:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        max_length = 1
        start = 0
        for i in range(len(s)):
            if i - max_length >= 1 and\
                s[i-max_length-1:i+1] == s[i-max_length-1:i+1][::-1]:
                start = i - max_length - 1
                max_length += 2
            elif i - max_length >= 0 and\
                s[i-max_length:i+1] == s[i-max_length:i+1][::-1]:
                start = i - max_length
                max_length += 1
        return s[start:start+max_length]
