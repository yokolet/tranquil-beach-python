import math

class Coins:
    def arrangeCoins(self, n: 'int') -> 'int':
        return int((-1 + math.sqrt(1 + 8 * n))/2)