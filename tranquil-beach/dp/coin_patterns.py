class CoinPatterns:
    def change(self, amount: 'int', coins: 'List[int]') -> 'int':
        memo = [0] * (amount + 1)
        memo[0] = 1 # when amount = 0, empty pattern exists
        for coin in coins:
            for i in range(coin, amount + 1):
                if memo[i - coin]:
                    memo[i] += memo[i - coin]
        return memo[amount]
