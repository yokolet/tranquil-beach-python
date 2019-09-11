class PackageShipping:
    def shipWithinDays(self, weights: 'List[int]', D: int) -> int:
        low, high = max(max(weights), sum(weights)//D), sum(weights)
        while low < high:
            mid = (low + high) // 2
            w_sum = 0
            days = 1
            for w in weights:
                w_sum += w
                if w_sum > mid:
                    w_sum = w
                    days += 1
            if days > D:
                low = mid + 1
            else:
                high = mid
        return low