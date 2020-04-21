class ConfusingNumberUptoN:
    def confusingNumberII(self, N: int) -> int:
        def symmetric(n):
            s = str(n)
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != mapping[s[r]]: return False
                l += 1
                r -= 1
            return True
        
        def dfs(n, count):
            if int(n) > N: return count
            if not symmetric(n):
                count += 1
            for c in '01689':
                count = dfs(n+c, count)
            return count

        mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        count = 0
        for i in '1689':
            count = dfs(i, count)
        return count
