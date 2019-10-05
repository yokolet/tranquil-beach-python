from collections import defaultdict
class Isomorphic:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        for i in range(len(s)):
            if s[i] in s2t:
                if s2t[s[i]] != t[i]: return False
            elif t[i] in s2t.values(): return False
            else: s2t[s[i]] = t[i]
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
