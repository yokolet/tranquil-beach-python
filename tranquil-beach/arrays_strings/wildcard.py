class Wildcard:
    def isMatch(self, s: str, p: str) -> bool:
        i, j, star_i, star_j = 0, 0, None, None
        while i < len(s):
            if j < len(p) and p[j] == '*':
                star_i, star_j = i, j
                j += 1
            elif j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif star_i is not None:
                i, j = star_i + 1, star_j + 1
                star_i += 1
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

    def isMatch4(self, s, p):
        si = pi = 0
        ssi = spi = None  # '*' indexes        
        sl, pl = len(s), len(p)
        while si < sl:
            if pi < pl and p[pi] == '*':
                ssi, spi = si, pi
                pi += 1                
            elif pi < pl and (p[pi] == s[si] or p[pi] == '?'):
                si, pi = si+1, pi+1
            elif spi is not None:
                si, pi = ssi+1, spi+1
                ssi += 1                
            else:
                return False

        while pi < pl and p[pi] == '*':
            pi += 1

        return pi == pl
            
    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        states = set([0])
        for c in p:
            nextStates = set()
            for state in states:
                if c == "*":
                    nextStates |= set(range(state, len(s)+1))
                if state >= len(s): continue
                if s[state] == c or c == "?":
                    nextStates.add(state + 1)
            states = nextStates
        for state in states:
            if state == len(s): return True
        return False

    def isMatch1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        transfer = {}
        state = 0
        
        for char in p:
            if char == '*':
                transfer[state, char] = state
            else:
                transfer[state, char] = state + 1
                state += 1
        
        accept = state
        state = set([0])
        
        for char in s:
            state = set([transfer.get((at, token)) for at in state for token in [char, '*', '?']])
        
        return accept in state

    def isMatch3(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        s_idx, p_idx = 0, 0
        s_start, p_start = 0, -1
        while s_idx < m:
            if p_idx < n and (s[s_idx] == p[p_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            elif p_idx < n and p[p_idx] == '*':
                s_start = s_idx
                p_start = p_idx
                p_idx += 1
            elif p_start != -1:
                s_start += 1
                s_idx = s_start
                p_idx = p_start + 1
            else:
                return False
        while p_idx < n and p[p_idx] == '*':
            p_idx += 1
        return s_idx == m and p_idx == n