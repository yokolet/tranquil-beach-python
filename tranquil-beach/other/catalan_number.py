class CatalanNumber:
    def numTrees(self, n: int) -> int:
        count = 1
        for i in range(1, n+1):
            count *= (n + i) / i
        return round(count / (n+1))
    
    def numTrees2(self, n: int) -> int:
        memo = {}
        memo[0] = 1
        memo[1] = 1
        
        def catalan(n):
            if n in memo: return memo[n]
            memo[n] = 0
            for i in range(n+1):
                memo[n] += catalan(i) * catalan(n-i-1)
            return memo[n]

        return catalan(n)
