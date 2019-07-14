from collections import deque

class EditDistance:
    def minDistance2(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        m, n = len(word1), len(word2)
        memo = [[0 for j in range(n+1)] for i in range(m+1)]
        # intialize
        for i in range(m+1):
            memo[i][0] = i
        for i in range(n+1):
            memo[0][i] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    memo[i][j] = memo[i-1][j-1]
                else:
                    replace = memo[i-1][j-1]+1
                    insert = memo[i][j-1]+1
                    delete = memo[i-1][j]+1
                    memo[i][j] = min(replace, insert, delete)
        return memo[m][n]

    def minDistance(self, word1: str, word2: str) -> int:
        seen = set()
        q = deque([(word1, word2, 0)])
        while q:
            (w1, w2, d) = q.popleft()
            if w1 == w2:
                return d
            if (w1, w2) in seen:
                continue
            else:
                seen.add((w1, w2))
            while w1 and w2 and w1[0] == w2[0]:
                w1 = w1[1:]
                w2 = w2[1:]
            q.append((w1, w2[1:], d + 1))       # remove
            q.append((w1[1:], w2, d + 1))       # insert
            q.append((w1[1:], w2[1:], d + 1))   # replace