class MinCoinChange:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i and (memo[i - coin] + 1 < memo[i]):
                    memo[i] = memo[i - coin] + 1
        return -1 if memo[amount] == float('inf') else memo[amount]

    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def dfs(amount, current_count, start_index):
            if current_count - (-amount//coins[start_index]) >= result[0]:
                return
            if amount % coins[start_index] == 0:
                result[0] = min(result[0], current_count + amount // coins[start_index])
                return
            if start_index == len(coins) - 1:
                return
            for i in range(amount//coins[start_index], -1, -1):
                dfs(amount - i*coins[start_index], current_count + i, start_index + 1)
            return  
        coins.sort(reverse = True)
        result = [amount + 1]
        dfs(amount, 0, 0)
        return result[0] if result[0] < amount + 1 else -1
