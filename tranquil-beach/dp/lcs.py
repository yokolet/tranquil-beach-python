class LCS:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m, n = len(text1), len(text2)
        prev = [0 for _ in range(n+1)]
        for i in range(m):
            cur = [0 for _ in range(n+1)]
            for j in range(n):
                if text1[i] == text2[j]:
                    cur[j+1] = prev[j]+1
                else:
                    cur[j+1] = max(prev[j+1], cur[j])
            prev = cur
        return cur[-1]

    # easy to understand but much slower
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    memo[i][j] = memo[i-1][j-1]+1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        return memo[m][n]
