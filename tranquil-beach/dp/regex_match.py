class RegexMatch:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def isMatchRecur(i: int, j:int) -> bool:
            if (i, j) not in memo:
                if j == len(p):
                    result = i == len(s)
                else:
                    result = i < len(s) and p[j] in ['.', s[i]]
                    if j + 1 < len(p) and p[j + 1] == '*':
                        result = isMatchRecur(i, j + 2) or (result and isMatchRecur(i + 1, j))
                    else:
                        result = result and isMatchRecur(i + 1, j + 1)
                memo[i, j] = result
            return memo[i, j]
        return isMatchRecur(0, 0)
    
    def isMatch5(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        memo = [[False] * (n + 1) for _ in range(m + 1)]
        memo[0][0] = True
        for i in range(1, n):
            memo[0][i + 1] = memo[0][i - 1] and p[i] == '*'
        for i in range(m):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    memo[i + 1][j] = memo[i + 1][j - 2] or memo[i + 1][j - 1]
                    if p[j - 2] == s[i] or p[j - 2] == '.':
                        memo[i + 1][j] |= memo[i][j]
                else:
                    memo[i + 1][j] = memo[i][j - 1] and (p[j - 1] == s[i] or p[j - 1] == '.')
        return memo[m][n]

    def isMatch2(self, s: 'str', p: 'str') -> 'bool':
        """
        Iterate through the pattern, matching as we go, recording
        all possible points (levels) in s, to which our match
        could have reached (so we don't greedy match).
        
        We check the last char in s and that the possible level
        is at the end of the string, at the very end.
        
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        
        levels_in_s = {0}
        for i, char_p in enumerate(p[:-1], 1):
            
            # False if no points match
            if not levels_in_s:
                return False
            
            # If the pattern character is "."
            if char_p == ".":
                
                # If we're at a Kleene star, add possible levels
                # from current lvl to the end of the string
                if p[i] == "*":
                    levels_in_s = set(range(min(levels_in_s),
                                            len(s)+1))
                # Add 1 to all possible levels
                else:
                    levels_in_s = {j+1 
                                   for j in levels_in_s 
                                   if j < len(s)}
            
            # If we're not at a Kleene Star
            elif char_p != "*":
                
                # If the next char is a Kleene Star, add possible
                # levels from current to highest possible level
                if p[i] == "*":
                    tmp = set()
                    for j in levels_in_s:
                        while j < len(s) and s[j] == char_p:
                            j += 1
                            tmp.add(j)
                    levels_in_s.update(tmp)
                
                # If the next char isn't a Kleene star, we must
                # match the char, and add 1 to all possible lvls
                else:
                    # Lvls only possible if < len(s) and they
                    # match the current character.
                    levels_in_s = {j + 1 
                        for j in levels_in_s
                        if j < len(s) and s[j] == char_p}
                             
        # If we have a Kleene star remaining, we match if
        # levels_in_s contains the length of the str. 
        if p[-1] == "*":
            return len(s) in levels_in_s

        # Are we at the end of s & does the last char match?
        else:
            return (len(s) - 1 in levels_in_s and 
                (s[-1] == p[-1] or "." == p[-1]))
        
    def isMatch3(self, s: 'str', p: 'str') -> 'bool':
        
        # Cannot match the Kleene star of nothing
        if p and p[0] == "*":
            return False
        
        # If pattern is empty, it's a match only if the text is empty
        if not p:
            return not s
        
        # Try matching the first character
        first_match = bool(s) and p[0] in {s[0], "."}
        
        # Otherwise, if there's a kleene star in the next char
        if len(p) >= 2 and p[1] == "*":
            
            # Either there's no repeats,     or there's at least one repeat
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        
        # Otherwise, match the rest of the string
        return first_match and self.isMatch(s[1:], p[1:])
 
    def isMatch4(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i: int, j: int) -> bool:
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    _match = i < len(s) and p[j] in ['.', s[i]]
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or (_match and dp(i + 1, j))
                    else:
                        ans = _match and dp(i + 1, j + 1)
                memo[i, j] = ans

            return memo[i, j]

        return dp(0, 0)
