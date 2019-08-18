class Compression:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        cur, prev = '', '1'
        for _ in range(n-1):
            count, p = 0, prev[0]
            for i in range(len(prev)):
                if prev[i] == p:
                    count += 1
                else:
                    cur += str(count) + p
                    count, p = 1, prev[i]
            cur += str(count) + p
            cur, prev = '', cur
        return prev
