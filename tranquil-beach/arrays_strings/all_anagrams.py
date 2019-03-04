from collections import Counter

class AllAnagrams:
    def findAnagrams(self, s: 'str', p: 'str') -> 'List[int]':
        if len(p) > len(s): return []
        target, counts, left, result = dict(Counter(p)), {}, 0, []

        for i in range(len(s)):
            if s[i] not in target:
                counts, left = {}, i + 1
                continue
            counts[s[i]] = counts.get(s[i], 0) + 1
            if i - left + 1 == len(p):
                if counts == target:
                    result.append(left)
                counts[s[left]] -= 1
                left += 1

        return result

    def findAnagrams4(self, s: str, p: str) -> 'List[int]':
        if len(s) < len(p):
            return []
        dic1 = [0]*26
        dic2 = [0]*26
        res = []
        for i in range(len(p)):
            dic1[ord(p[i])-ord('a')] += 1
            dic2[ord(s[i])-ord('a')] += 1
        if dic1 == dic2:
            res.append(0)
        for i in range(1, len(s)-len(p)+1):
            dic2[ord(s[i-1])-ord('a')] -= 1
            dic2[ord(s[i+len(p)-1])-ord('a')] += 1
            if dic1 == dic2:
                res.append(i)
        return res
