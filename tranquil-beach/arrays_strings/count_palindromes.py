class CountPalindromes:
    def countSubstrings(self, s: 'str') -> 'int':
        if not s: return 0
        result, left = 0, 0
        while left < len(s):
            right = left + 1
            while right < len(s) and s[left] == s[right]:
                right += 1
            result += (right-left) * (right-left+1) // 2
            l = left - 1
            r = right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                result += 1
            left = right
        return result

    def countSubstrings3(self, s: str) -> int:
        C, R = 0, 0
        T = "@#" + "#".join(s) + "#$"
        P = [0]*len(T) # saves radius at index i
        for i in range(1, len(T)-1):
            if i < R:
                P[i] = min(P[2*C-i], R-i)
            while T[i-P[i]-1] == T[i+P[i]+1]:
                P[i] += 1
            if i+P[i] > R:
                C, R = i, i + P[i]
        return sum((x+1)//2 for x in P)
