class DecodeDigits:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0': return 0
        n = len(s)
        memo = [0]*(n + 1)
        memo[0] = 1 # s is empty
        memo[1] = 1 # s[0] is 1 to 9
        for i in range(2, n+1):
            ones, tens = s[i - 1], s[i - 2]
            if ones >= '1' and ones <= '9':
                memo[i] += memo[i - 1]
            if tens == '1' or (tens == '2' and ones <= '6'):
                memo[i] += memo[i - 2]
        return memo[n]

    def numDecodings3(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        # dp = [0] * (n + 1)
        # dp[n] = 1
        # dp[n - 1] = 0 if s[n - 1] == "0" else 1
        first = 1
        second = 0 if s[n-1] == "0" else 1

        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                first = second
                second = 0
            else:
                if s[i:i + 2] <= "26":
                    # dp[i] = dp[i + 1] + dp[i + 2]
                    current = first + second
                    first = second
                    second = current
                else:
                    # dp[i] = dp[i + 1]
                    first = second
        # return dp[0]
        return second
        