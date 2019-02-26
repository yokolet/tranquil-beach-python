class PalindromeByDeletion:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n <= 2 or s == s[::-1]: return True
        left, right = 0, n - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return s[left+1:right+1] == s[left+1:right+1][::-1] or\
                        s[left:right] == s[left:right][::-1]
        return True

    # faster
    def validPalindrome2(self, s: 'str') -> 'bool':
        sReversed = s[::-1]
        if s == sReversed: return True
        else:
            for i in range(len(s)):
                if s[i] != sReversed[i]:
                    if i == len(s)-1: return True
                    return s[i+1:] == sReversed[i:len(s)-1-i] + sReversed[len(s)-i:] or\
                             s[i:len(s)-1-i] + s[len(s)-i:] == sReversed[i+1:]