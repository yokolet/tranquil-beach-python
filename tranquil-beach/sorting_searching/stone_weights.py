import heapq

class StoneWeights:
    def lastStoneWeight(self, stones: 'List[int]') -> int:
        stones  = [-v for v in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            diff = abs(a - b)
            if diff > 0:
                heapq.heappush(stones, -diff)
        return 0 if len(stones) == 0 else -stones[0]
