class StringShifts:
    def stringShift(self, s: str, shift: 'List[List[int]]') -> str:
        counts = [0, 0]
        for d, a in shift:
            counts[d] += a
        total = counts[0] - counts[1]
        if total == 0:
            return s
        elif total < 0:
            total = abs(total) % len(s)
            return s[-total:]+s[:-total]
        else:
            total = total % len(s)
            return s[total:]+s[:total]