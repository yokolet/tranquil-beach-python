from collections import defaultdict

class HandOfStraights:
    def isNStraightHand(self, hand: 'List[int]', W: int) -> bool:
        if W == 1: return True
        if len(hand) % W != 0: return False
        num_dict = defaultdict(int)
        for num in hand:
            num_dict[num] += 1
        for n in sorted(set(hand)):
            count = num_dict[n]
            if count == 0: continue
            for i in range(n, n+W):
                if i not in num_dict or num_dict[i] < count: return False
                num_dict[i] -= count
        return True