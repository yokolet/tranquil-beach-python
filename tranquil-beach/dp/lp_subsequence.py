class LongestPalindromicSubsequence:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if s == s[::-1]: return n
        prev = [0] * n
        for i in range(n-1, -1, -1):
            cur = [0] * n
            cur[i] = 1
            for l in range(i+1, n):
                if s[i] == s[l]:
                    cur[l] = prev[l-1] + 2
                else:
                    cur[l] = max(prev[l], cur[l-1])
            prev = cur
        return prev[-1]

    # very slow
    def longestPalindromeSubseq3(self, s: str) -> int:
        n = len(s)
        if s == s[::-1]: return n
        memo = [[0] * n for _ in range(n)]
        # base case - a single char is a palindrome
        for i in range(n):
            memo[i][i] = 1
        # fill the rest
        for l in range(2, n+1): # length
            for i in range(n - l + 1): # starting index i
                j = i + l - 1 # ending index j
                if l == 2 and s[i] == s[j]:
                    memo[i][j] = 2
                elif s[i] == s[j]:
                    memo[i][j] = memo[i+1][j-1] + 2
                else:
                    memo[i][j] = max(memo[i][j-1], memo[i+1][j])
        return memo[0][n-1]

    # fast
    def longestPalindromeSubseq4(self, s: 'str') -> 'int':
        N = len(s)
        if N < 2 or s == s[::-1]:
            return N
        prev = [1]*N
        dp = [1 + (s[l] == s[l+1]) for l in range(N-1)]
        for idiff in range(2, N):
            prev, dp = dp, [2+prev[l+1] if s[l] == s[l+idiff] else max(dp[l+1], dp[l]) for l in range(N-idiff)]
        return dp[0]