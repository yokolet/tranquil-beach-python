class DivideChocolate:
    def maximizeSweetness(self, sweetness: 'List[int]', K: int) -> int:
        if len(sweetness) == K+1: return min(sweetness)
        low, high = min(sweetness), sum(sweetness)//(K+1)
        while low < high:
            mid = (low + high + 1) // 2
            s_sum, cuts = 0, 0
            for s in sweetness:
                s_sum += s
                if s_sum >= mid:
                    s_sum = 0
                    cuts += 1
            if cuts > K:
                low = mid
            else:
                high = mid - 1
        return high
