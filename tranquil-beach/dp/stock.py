class Stock:
    def maxProfit(self, prices: 'List[int]') -> int:
        profit, min_price = 0, float('inf')
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > profit:
                profit = p - min_price
        return profit
