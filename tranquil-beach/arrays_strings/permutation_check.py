from collections import defaultdict

class PermutationCheck:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = defaultdict(int)
        for c in s1:
            target[c] += 1
        left, counts = 0, defaultdict(int)
        for i in range(len(s2)):
            if s2[i] not in target:
                counts, left = defaultdict(int), i + 1
                continue
            counts[s2[i]] += 1
            if i-left+1 == len(s1):
                if counts == target: return True
                counts[s2[left]] -= 1
                left += 1
        return False