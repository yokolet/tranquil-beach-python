class Stairs:
    def climbStairsRecur(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0: return 0
        if n == 0: return 1
        sum = 0
        sum += self.climbStairsRecur(n-1)
        sum += self.climbStairsRecur(n-2)
        return sum

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0]*(n+1)
        memo[0] = 1
        memo[1] = 1
        for i in range(2, n+1):
            j = 1
            while j <= 2 and j <= i:
                memo[i] += memo[i-j]
                j += 1
        return memo[n]